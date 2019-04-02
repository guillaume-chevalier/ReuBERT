from typing import List, Dict, Tuple

from src.domain.pipeline_steps.question_answering_model_interface import QuestionAnsweringModelInterface, \
    TextQuestionAnswerTriplet
from src.infrastructure.pipeline_steps.trained_bert_q_a_model import TrainedBERTQuestionAnsweringModel, \
    get_reubert_flags

UserInputAndQuestionTuple = Tuple[List[str], str]

# TODO Taha: maybe that the above `UserInputAndQuestionTuple` type is just like this instead, I'm not sure of what you did:
# TODO Taha:     UserInputAndQuestionTuple = Tuple[str, str]


class BertModelWrapper(QuestionAnsweringModelInterface):

    def __init__(self):
        self.bert_model = TrainedBERTQuestionAnsweringModel(get_reubert_flags())

    def _from_normal_input_to_bert_input_dict(self, normal_input):
        joined_user_inputs = "".join(normal_input["user_input"])
        return [
            {
                "paragraphs": [
                    {
                        "context": joined_user_inputs,
                        "qas":
                        [{
                            "answers": [],
                            "id": "",
                            "is_impossible": False,
                            "question": normal_input["question"]
                        }]
                    }
                ],
                "title":
                ""
            }
        ]

    def _from_bert_output_to_normal_output(self, all_nbest_json):
        return [(y['probability'], y['text']) for y in [x[1] for x in all_nbest_json.items()][0]]

    @staticmethod
    def question_schema(user_input, question) -> Dict[str, str]:
        return {"user_input": user_input, "question": question}

    def transform(self, X: List[UserInputAndQuestionTuple]) -> List[TextQuestionAnswerTriplet]:
        # TODO Taha: do `for user_input, question in X:` instead. Pipelines are meant to process arrays of things.
        # TODO Taha: see the class `BertNaturalAnswerPostprocessor` for an example of this for loop.
        transformed_output = self.process_one(X)
        # TODO Taha: return triplets of TextQuestionAnswerTriplet, as seen in `BertNaturalAnswerPostprocessor`.
        return transformed_output  # The return type must be a list.

    def process_one(self, X: UserInputAndQuestionTuple) -> TextQuestionAnswerTriplet:
        user_input, question = X
        normal_input = BertModelWrapper.question_schema(user_input, question)
        transformed_input = self._from_normal_input_to_bert_input_dict(normal_input)
        _, all_nbest_json, _ = self.bert_model.transform(transformed_input)
        transformed_output = self._from_bert_output_to_normal_output(all_nbest_json)
        return transformed_output
