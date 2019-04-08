import pytest
import os
import json

from src.domain.pipeline_steps.best_answer_extractor import BestAnswerExtractor
from src.util.ResponseEvaluator import ResponseEvaluator

def load_json_file_test(json_name):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), json_name), encoding="utf8") as json_data:
        return json.load(json_data)


QUESTION_TYPES = ["where", "when", "who", "why", "which", "whom", "whose", "what", "how_far", "how_long",
                  "how_many",
                  "how_much", "how_old"]


class TestBestAnswerExtractor():
    @classmethod
    def setup_class(self):
        self.TEXT_AND_QUESTIONS_MOCK = load_json_file_test('answer_selector_mock_questions.json')

        self.best_answer_extractor = BestAnswerExtractor()
        self.user_input = self.TEXT_AND_QUESTIONS_MOCK["text"]

    @pytest.mark.parametrize("type", QUESTION_TYPES)
    @pytest.mark.parametrize("test_num", [0, 1])
    def test__given__answers_and_wh_questions__when__bert_answer_extrator__then__choose_best_response(self, type,
                                                                                                      test_num):
        question = self.TEXT_AND_QUESTIONS_MOCK["WH"][type][test_num][0]
        answers = self.TEXT_AND_QUESTIONS_MOCK["WH"][type][test_num][1]
        right_res = self.TEXT_AND_QUESTIONS_MOCK["WH"][type][test_num][2]

        response = self.best_answer_extractor.extract_best_answer(self.user_input, question, answers)
        print("Question : ", question)
        print("Bert answers : ", answers)
        assert self.response_is_close_enough(response, right_res)

    def response_is_close_enough(self, response, expected_res):
        print("Extracted answer : ", response)
        response_evalluator = ResponseEvaluator()
        return response_evalluator.is_response_close_enough(response, expected_res)
