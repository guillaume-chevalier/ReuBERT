from src.infrastructure.user_input_question_pair import UserInputQuestionPair


class BertModelWrapper:

    def __init__(self, bert_model):
        self.bert_model = bert_model

    def _from_normal_input_to_bert_input_dict(self, normal_input):
        return [
            {
                "paragraphs": [
                    {
                        "context": normal_input.get_user_input(),
                        "qas":
                        [{
                            "answers": [],
                            "id": "",
                            "is_impossible": False,
                            "question": normal_input.get_question()
                        }]
                    }
                ],
                "title":
                ""
            }
        ]

    def _from_bert_output_to_normal_output(self, all_nbest_json):
        return [(y['probability'], y['text']) for y in [x[1] for x in all_nbest_json.items()][0]]

    def transform(self, user_input_question_pair: UserInputQuestionPair):
        transformed_input = self._from_normal_input_to_bert_input_dict(user_input_question_pair)
        _, all_nbest_json, _ = self.bert_model.transform(transformed_input)
        transformed_output = self._from_bert_output_to_normal_output(all_nbest_json)
        return transformed_output
