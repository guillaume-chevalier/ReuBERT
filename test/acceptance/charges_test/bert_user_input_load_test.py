import json
import os
import stringdist

from src.infrastructure.pipeline_steps.bert_model_wrapper import BertModelWrapper


def load_json_file_test(json_name):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), json_name), encoding="utf8") as json_data:
        return json.load(json_data)


SQUAD_TEST_FILE = load_json_file_test('../../../thales-bert-gcp-bucket/squad_dir/squad_questions_beautified.json')


# Todo: still uncomplete maybe useful for the report or the presentation to see how bert reacts to different input text length

def run_bert_user_input_load_test():
    for elem in SQUAD_TEST_FILE:
        sections = elem["qa"]
        user_input, questions = get_proportion(sections, )
        bert_wrapper = BertModelWrapper()
        response = bert_wrapper.transform((user_input, question))

        verify_answers(response, expected_answers)


def get_proportion(sections, portion):
    portion = int(portion * len(sections))
    text = [sections[i]["qa"]["subtext"] for i in range(portion)]
    questions = [sections[i]["qa"]["qas"] for i in range(portion)]
    flat_question_list = [item for sublist in questions for item in sublist]
    return text, flat_question_list


def verify_answers(bert_responses, expected_responses):
    right_answer = None
    acceptable_levenshtein_threshold = 0.5

    for bert_res in bert_responses:
        for expected_res in expected_responses:
            if stringdist.levenshtein(bert_res[1], expected_res) / 33 < acceptable_levenshtein_threshold:
                right_answer = bert_res

    assert right_answer is not None
