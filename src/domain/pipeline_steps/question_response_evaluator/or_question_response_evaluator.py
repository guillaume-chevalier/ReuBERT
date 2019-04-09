import en_core_web_sm

from src.domain.pipeline_steps.question_response_evaluator.question_type_analyser import QuestionTypeFinder
from src.util.response_evaluator import ResponseEvaluator

nlp = en_core_web_sm.load()


class ORQuestionResponseEvaluator:

    def __init__(self):
        super().__init__()
        self.question_type_finder = QuestionTypeFinder()

    def extract_best_answer(self, or_question, bert_answers):
        ors_responses = self._determine_type_of_expected_response_from_OR_question(or_question)
        extract_ans = self._extract_or_answer(bert_answers, ors_responses)
        if extract_ans:
            return extract_ans
        else:
            return self._extract_from_uncertain_answers(bert_answers)

    def _extract_from_uncertain_answers(self, bert_answers):
        best_answer = [0, ""]
        for answer in bert_answers:
            if answer[0] > best_answer[0]:
                best_answer[0] = answer[0]
                best_answer[1] = answer[1]
        return best_answer[1]

    def _determine_type_of_expected_response_from_OR_question(self, or_question):
        tokenized_or_question = self._tokenize(or_question)
        ors = []
        for index in range(len(tokenized_or_question)):
            if self.question_type_finder.is_or_word(tokenized_or_question[index]):
                ors.append(tokenized_or_question[index - 1])
                ors.append(tokenized_or_question[index + 1])

        return ors

    def _extract_or_answer(self, bert_answers, ors):
        response_evaluator = ResponseEvaluator()
        for bert_res in bert_answers:
            for or_res in ors:
                if response_evaluator.is_response_close_enough_using_leveinstein(bert_res[1], or_res):
                    return bert_res

    def _tokenize(self, sent):
        return nlp(sent).ents

    def _extract_responses_only(self, bert_response):
        return [answer[1] for answer in bert_response]
