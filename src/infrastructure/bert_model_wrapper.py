class BertModelWrapper:
    def __init__(self, bert_model):
        self.bert_model = bert_model

    def from_normal_input_bert_input(self, normal_input):
        return [{
            "paragraphs": [
                {
                    "context": normal_input["user_input"],
                    "qas": [
                        {
                            "answers": [
                                {
                                    "answer_start": 159,
                                    "text": "France"
                                },
                                {
                                    "answer_start": 159,
                                    "text": "France"
                                },
                                {
                                    "answer_start": 159,
                                    "text": "France"
                                },
                                {
                                    "answer_start": 159,
                                    "text": "France"
                                }
                            ],
                            "id": "56ddde6b9a695914005b9628",
                            "is_impossible": False,
                            "question": normal_input["question"]
                        }
                    ]
                }
            ],
            "title": "Normans"
        }]

    def from_bert_output_to_normal_output(self, all_nbest_json):
        return [(y['probability'], y['text']) for y in [x[1] for x in all_nbest_json.items()][0]]

    def transform(self, normal_input):
        transformed_input = self.from_normal_input_bert_input(normal_input)
        _, all_nbest_json, _ = self.bert_model.transform(transformed_input)
        transformed_output = self.from_bert_output_to_normal_output(all_nbest_json)
        return transformed_output
