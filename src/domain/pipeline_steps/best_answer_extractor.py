import re

from src.domain.pipeline_steps.question_response_evaluator.or_question_response_evaluator import \
    ORQuestionResponseEvaluator
from src.domain.pipeline_steps.question_response_evaluator.wh_question_response_evaluator import \
    WHQuestionResponseEvaluator
from src.domain.pipeline_steps.question_response_evaluator.yesno_question_response_evaluator import \
    YESNOQuestionProcessor


class BestAnswerExtractor():
    _WH_WORDS_REGEX = r'who|what|how|where|when|why|which|whom|whose'
    _OR_REGEX = r'or'

    def __init__(self):
        self.or_question_processor = ORQuestionResponseEvaluator()
        self.wh_question_processor = WHQuestionResponseEvaluator()
        self.yesno_question_processor = YESNOQuestionProcessor()

    def extract_best_answer(self, user_input, question, bert_answers):

        bert_answers = self._extract_responses_only(bert_answers)

        if re.search(self._WH_WORDS_REGEX, question.lower()):
            return self.wh_question_processor.extract_best_answer(user_input, question, bert_answers)

        if re.search(self._OR_REGEX, question.lower()):
            return self.or_question_processor.extract_best_answer(question, bert_answers)

        else:
            return self.yesno_question_processor.extract_best_answer(question, bert_answers)

    def _extract_responses_only(self, bert_response):
        return [answer[1] for answer in bert_response]
