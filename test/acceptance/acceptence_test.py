import json
import os

import pytest
import stringdist

from src.infrastructure.bert_model_wrapper import BertModelWrapper
from src.infrastructure.trained_bert_q_a_model import TrainedBERTQuestionAnsweringModel, get_reubert_flags

flags = get_reubert_flags()
bert_model = TrainedBERTQuestionAnsweringModel(flags)

bert_wrapper = BertModelWrapper(bert_model)


# Todo : put different levels of questions : easy , medium, hard, impossible
def load_json_file_test(json_name):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), json_name), encoding="utf8") as json_data:
        return json.load(json_data)


QATEST_FILE_1 = load_json_file_test('QA_test_1.json')
QATEST_FILE_2 = load_json_file_test('QA_test_2.json')
QATEST_FILE_3 = load_json_file_test('QA_test_3.json')


@pytest.mark.parametrize("QA_test", [QATEST_FILE_1])
@pytest.mark.parametrize("difficulty", ["easy"])
def test__given__user_input__when__asking_questions_to_bert_model_wrapper__then__get_good_results(QA_test, difficulty):
    user_input = QA_test['user_inputs']

    question_1 = QA_test['QA'][difficulty][0]['question']
    expected_answers_1 = QA_test['QA'][difficulty][0]['answers']

    question_2 = QA_test['QA'][difficulty][1]['question']
    expected_answers_2 = QA_test['QA'][difficulty][1]['answers']

    question_3 = QA_test['QA'][difficulty][2]['question']
    expected_answers_3 = QA_test['QA'][difficulty][2]['answers']

    question_4 = QA_test['QA'][difficulty][3]['question']
    expected_answers_4 = QA_test['QA'][difficulty][3]['answers']

    response_1 = bert_wrapper.transform(bert_wrapper.question_schema(user_input, question_1))
    response_2 = bert_wrapper.transform(bert_wrapper.question_schema(user_input, question_2))
    response_3 = bert_wrapper.transform(bert_wrapper.question_schema(user_input, question_3))
    response_4 = bert_wrapper.transform(bert_wrapper.question_schema(user_input, question_4))

    verify_answers(response_1, expected_answers_1)
    verify_answers(response_2, expected_answers_2)
    verify_answers(response_3, expected_answers_3)
    verify_answers(response_4, expected_answers_4)


def verify_answers(bert_responses, expected_responses):
    right_answer = None
    acceptable_levenshtein_threshold = 0.5

    for bert_res in bert_responses:
        for expected_res in expected_responses:
            if stringdist.levenshtein_norm(bert_res[1], expected_res) < acceptable_levenshtein_threshold:
                right_answer = bert_res

    assert right_answer is not None
