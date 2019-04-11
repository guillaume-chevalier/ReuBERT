from src.infrastructure.pipeline_steps.bert_model_wrapper import BertModelWrapper
from src.infrastructure.pipeline_steps.bert_natural_answer_postprocessor import BertNaturalAnswerPostprocessor
from src.util.response_evaluator import ResponseEvaluator

import os
import json


def extract_question_from_squad():
    with open(os.path.join(__file__, '../squad_questions_beautified.json'), encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


bert_wrapper = BertModelWrapper()
best_post_processor = BertNaturalAnswerPostprocessor()
bert_evaluator = ResponseEvaluator()


def bert_with_squad_test():
    total_qu = 0
    good_res_bert_only = 0
    good_res_with_postprocessing = 0
    data = extract_question_from_squad()
    for elem in data:
        for el in elem['qa']:
            story = el['subtext']
            for qas in el['qas']:
                question = qas['question']
                answers = qas['answers']

                total_qu += 1

                output = bert_wrapper.transform_one(([story], question))

                transformed_answer = best_post_processor.transform_one(output)

                best_bert_ans = output[2][0][1]

                print('\n')
                print("number :", total_qu)
                # print("story :", story)
                if check_answers(best_bert_ans, answers):
                    good_res_bert_only += 1
                    print("bert only success")
                else:
                    print("bert only failed")

                if check_answers(transformed_answer, answers):
                    good_res_with_postprocessing += 1
                    print("bert with postprocessing success")
                else:
                    print("bert with postprocessing failed")

                print("Question:", question)
                print("possible answers:", answers)
                print("bert answer:", output[2])
                print("bert best guess:", best_bert_ans)
                print("transformed answer:", transformed_answer)
                print("accuracy without postprocessing :", good_res_bert_only / total_qu)
                print("accuracy with postprocessing :", good_res_with_postprocessing / total_qu)


def check_answers(best_bert_ans, answers):
    for answer in answers:
        if bert_evaluator.is_response_close_enough_using_difflib(best_bert_ans, answer):
            return answers
    return False


bert_with_squad_test()