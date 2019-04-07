from typing import List, Dict, Union

from src.domain.pipeline_steps.question_answering_model import QuestionAnsweringModel, \
    TextQuestionAnswerTriplet, UserInputAndQuestionTuple
from src.infrastructure.pipeline_steps.trained_bert_q_a_model import TrainedBERTQuestionAnsweringModel, \
    get_reubert_flags


class BertModelWrapper(QuestionAnsweringModel):

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
    def question_schema(user_input: List[str], question: str) -> Dict[str, Union[List[str], str]]:
        return {"user_input": user_input, "question": question}

    def fit(self, X: List[UserInputAndQuestionTuple]) -> 'BertModelWrapper':
        return self

    def transform(self, X: List[UserInputAndQuestionTuple]) -> List[TextQuestionAnswerTriplet]:
        transformed_output = [self.transform_one(user_input) for user_input in X]
        return transformed_output

    def transform_one(self, X: UserInputAndQuestionTuple) -> TextQuestionAnswerTriplet:
        user_input, question = X
        normal_input = BertModelWrapper.question_schema(user_input, question)
        transformed_input = self._from_normal_input_to_bert_input_dict(normal_input)
        _, all_nbest_json, _ = self.bert_model.transform(transformed_input)
        transformed_output = self._from_bert_output_to_normal_output(all_nbest_json)
        return (user_input, question, transformed_output)
