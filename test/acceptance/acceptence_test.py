import json
import os

import pytest

# Todo : put different levels of questions : easy , meduim, hard, impossible
def load_json_file_test(json_name):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), json_name), encoding="utf8") as json_data:
        return json.load(json_data)


QATEST_FILE_1 = load_json_file_test('QA_test_1.json')
QATEST_FILE_2 = load_json_file_test('QA_test_2.json')
QATEST_FILE_3 = load_json_file_test('QA_test_3.json')


# load model
# Model = None

@pytest.mark.parametrize("QA_test", [QATEST_FILE_1, QATEST_FILE_2, QATEST_FILE_3])
def test_model_answer_test_1(QA_test):
    user_input = QA_test['user_inputs']

    question_1 = QA_test['QA'][0]['question']
    answers_1 = QA_test['QA'][0]['answers']

    question_2 = QA_test['QA'][1]['question']
    answers_2 = QA_test['QA'][1]['answers']

    question_3 = QA_test['QA'][2]['question']
    answers_3 = QA_test['QA'][2]['answers']

    question_4 = QA_test['QA'][3]['question']
    answers_4 = QA_test['QA'][3]['answers']

    # Model.load(user_input)

    # response_1 = Model.answer(question_1)
    # response_2 = Model.answer(question_2)
    # response_3 = Model.answer(question_3)
    # response_4 = Model.answer(question_4)

    # assert response_1 in answers_1
    # assert response_2 in answers_2
    # assert response_3 in answers_3
    # assert response_4 in answers_4
    assert True
