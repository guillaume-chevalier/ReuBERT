import json
import os

import pytest

from src.domain.pipeline_steps.question_answering_model import UserInputAndQuestionTuple
from src.util.ResponseEvaluator import ResponseEvaluator
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
        expected_answers = (user_input, question, QA_test['QA'][difficulty][question_number]['answers'])

        input: UserInputAndQuestionTuple = [(user_input, question)]

        response = TestAcceptance.bert_wrapper.transform(input)

        verify_answers(response, expected_answers)


def verify_answers(bert_responses, expected_responses):
    response_evaluator = ResponseEvaluator()
    right_answer = None

    for bert_res in bert_responses:
        for expected_res in expected_responses:
            if response_evaluator.is_response_close_enough(bert_res[1], expected_res):
                right_answer = bert_res

    assert right_answer is not None
