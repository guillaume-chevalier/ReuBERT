import copy

from src.domain.pipeline_steps.question_response_evaluator.or_question_response_evaluator import \
    ORQuestionResponseEvaluator
from src.domain.pipeline_steps.question_response_evaluator.wh_question_response_evaluator import \
    WHQuestionResponseEvaluator

from src.domain.pipeline_steps.question_response_evaluator.question_type_analyser import QuestionTypeFinder


class BestAnswerExtractor():

    def __init__(self):
        self.or_question_processor = ORQuestionResponseEvaluator()
        self.wh_question_processor = WHQuestionResponseEvaluator()
        self.question_type_finder = QuestionTypeFinder()

    def extract_best_answer(self, user_input, question, bert_answers):

        extracted_answer = None

        if self.question_type_finder.is_wh_question(question):
            extracted_answer = self.wh_question_processor.extract_best_answer(user_input, question, bert_answers)

        elif self.question_type_finder.is_or_question(question):
            extracted_answer = self.or_question_processor.extract_best_answer(question, bert_answers)

        if extracted_answer:
            return extracted_answer

        else:
            extracted_answer = self._extract_from_uncertain_answers(bert_answers)

        return extracted_answer

    def _extract_from_uncertain_answers(self, bert_answers):
        best_answer = [0, '']
        for answer in bert_answers:
            if answer[0] > best_answer[0] and answer[1] != '':
                best_answer = copy.deepcopy(answer)
        return best_answer[1]
