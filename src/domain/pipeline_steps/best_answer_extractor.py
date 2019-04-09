from src.domain.pipeline_steps.question_response_evaluator.or_question_response_evaluator import \
    ORQuestionResponseEvaluator
from src.domain.pipeline_steps.question_response_evaluator.wh_question_response_evaluator import \
    WHQuestionResponseEvaluator
from src.domain.pipeline_steps.question_response_evaluator.yesno_question_response_evaluator import \
    YESNOQuestionProcessor

from src.domain.pipeline_steps.question_response_evaluator.question_type_analyser import QuestionTypeFinder


class BestAnswerExtractor():

    def __init__(self):
        self.or_question_processor = ORQuestionResponseEvaluator()
        self.wh_question_processor = WHQuestionResponseEvaluator()
        self.yesno_question_processor = YESNOQuestionProcessor()
        self.question_type_finder = QuestionTypeFinder()

    def extract_best_answer(self, user_input, question, bert_answers):

        if self.question_type_finder.is_wh_question(question):
            return self.wh_question_processor.extract_best_answer(user_input, question, bert_answers)

        if self.question_type_finder.is_or_question(question):
            return self.or_question_processor.extract_best_answer(question, bert_answers)

        else:
            return self.yesno_question_processor.extract_best_answer(question, bert_answers)


