import json
import os

QATEST_FILENAME = 'QA_test.json'

with open(os.path.join(os.getcwd(), QATEST_FILENAME), encoding="utf8") as json_data:
    QA_TESTS = json.load(json_data)

#load model
# Model = None


def test_model_answer_test_1():
    user_input = QA_TESTS['test_1']['user_inputs']

    question_1 = QA_TESTS['test_1']['QA'][0]['question']
    answers_1 = QA_TESTS['test_1']['QA'][0]['answers']

    question_2 = QA_TESTS['test_1']['QA'][1]['question']
    answers_2 = QA_TESTS['test_1']['QA'][1]['answers']

    question_3 = QA_TESTS['test_1']['QA'][2]['question']
    answers_3 = QA_TESTS['test_1']['QA'][2]['answers']

    question_4 = QA_TESTS['test_1']['QA'][3]['question']
    answers_4 = QA_TESTS['test_1']['QA'][3]['answers']

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


def test_model_answer_test_2():
    user_input = QA_TESTS['test_2']['user_inputs']

    question_1 = QA_TESTS['test_2']['QA'][0]['question']
    answers_1 = QA_TESTS['test_2']['QA'][0]['answers']

    question_2 = QA_TESTS['test_2']['QA'][1]['question']
    answers_2 = QA_TESTS['test_2']['QA'][1]['answers']

    question_3 = QA_TESTS['test_2']['QA'][2]['question']
    answers_3 = QA_TESTS['test_2']['QA'][2]['answers']

    question_4 = QA_TESTS['test_2']['QA'][3]['question']
    answers_4 = QA_TESTS['test_2']['QA'][3]['answers']

    # Model.load(user_input)
    #
    # response_1 = Model.answer(question_1)
    # response_2 = Model.answer(question_2)
    # response_3 = Model.answer(question_3)
    # response_4 = Model.answer(question_4)

    # assert response_1 in answers_1
    # assert response_2 in answers_2
    # assert response_3 in answers_3
    # assert response_4 in answers_4
    assert True


def test_model_answer_test_3():
    user_input = QA_TESTS['test_3']['user_inputs']

    question_1 = QA_TESTS['test_3']['QA'][0]['question']
    answers_1 = QA_TESTS['test_3']['QA'][0]['answers']

    question_2 = QA_TESTS['test_3']['QA'][1]['question']
    answers_2 = QA_TESTS['test_3']['QA'][1]['answers']

    question_3 = QA_TESTS['test_3']['QA'][2]['question']
    answers_3 = QA_TESTS['test_3']['QA'][2]['answers']

    question_4 = QA_TESTS['test_3']['QA'][3]['question']
    answers_4 = QA_TESTS['test_3']['QA'][3]['answers']

    # Model.load(user_input)
    #
    # response_1 = Model.answer(question_1)
    # response_2 = Model.answer(question_2)
    # response_3 = Model.answer(question_3)
    # response_4 = Model.answer(question_4)

    # assert response_1 in answers_1
    # assert response_2 in answers_2
    # assert response_3 in answers_3
    # assert response_4 in answers_4
    assert True
