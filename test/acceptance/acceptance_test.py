import json
import os

import pytest
import stringdist

from src.infrastructure.pipeline_steps.bert_model_wrapper import BertModelWrapper

# Todo : put different levels of questions : easy , medium, hard, impossible


def load_json_file_test(json_name):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), json_name), encoding="utf8") as json_data:
        return json.load(json_data)


QATEST_FILE_1 = load_json_file_test('QA_test_1.json')
QATEST_FILE_2 = load_json_file_test('QA_test_2.json')
QATEST_FILE_3 = load_json_file_test('QA_test_3.json')


class TestAcceptance():

    @classmethod
    def setup_class(cls):
        cls.bert_wrapper = BertModelWrapper()

    @pytest.mark.parametrize("QA_test", [QATEST_FILE_1, QATEST_FILE_2, QATEST_FILE_3])
    @pytest.mark.parametrize("difficulty", ["easy", "hard", "impossible"])
    @pytest.mark.parametrize("question_number", [0, 1, 2, 3])
    def test__given__user_input__when__asking_questions_to_bert_model_wrapper__then__get_good_results(
        cls, QA_test, difficulty, question_number
    ):
        user_input = QA_test['user_inputs']

        question = QA_test['QA'][difficulty][question_number]['question']
        expected_answers = QA_test['QA'][difficulty][question_number]['answers']

        response = TestAcceptance.bert_wrapper.transform((user_input, question))

        verify_answers(response, expected_answers)


def verify_answers(bert_responses, expected_responses):
    right_answer = None
    acceptable_levenshtein_threshold = 0.5

    for bert_res in bert_responses:
        for expected_res in expected_responses:
            if stringdist.levenshtein(bert_res[1], expected_res) / 33 < acceptable_levenshtein_threshold:
                right_answer = bert_res

    assert right_answer is not None
