import os
import json
import time

from src.infrastructure.pipeline_steps.bert_model_wrapper import BertModelWrapper
from src.infrastructure.pipeline_steps.bert_natural_answer_postprocessor import BertNaturalAnswerPostprocessor


def load_json_file_test(json_name):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), json_name), encoding="utf8") as json_data:
        return json.load(json_data)


num_words = [
    '50', '100', '150', '200', '250', '300', '350', '400', '450', '500', '550', '600', '650', '700', '750', '800',
    '850', '900', '950', '1000'
]


def run_load_test():
    mock_test_file = load_json_file_test('load_tests_file_mock.json')
    bert_wrapper = BertModelWrapper()
    best_post_processor = BertNaturalAnswerPostprocessor()

    for num_word in num_words:
        start_time = time.time()
        print('----------------------------')
        print('load test with ', num_word, ' words')
        print('started : ', start_time)
        input = mock_test_file[num_word]['input']
        question = mock_test_file[num_word]['question']

        print('question : ', question)

        output = bert_wrapper.transform_one(([input], question))

        transformed_answer = best_post_processor.transform_one(output)

        print('answer : ', transformed_answer)

        finish_time = time.time()
        taken_time = finish_time - start_time

        print('finished : ', finish_time)
        print('it took in sec : ', taken_time)


run_load_test()
