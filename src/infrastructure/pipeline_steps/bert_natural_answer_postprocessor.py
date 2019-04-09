from typing import List

from src.domain.pipeline_steps.natural_answer_postprocessor import NaturalAnswerPostprocessor
from src.domain.pipeline_steps.question_answering_model import TextQuestionAnswerTriplet
from src.domain.pipeline_steps.question_answering_model import BeautifiedAnswer
from src.domain.pipeline_steps.best_answer_extractor import BestAnswerExtractor
from src.domain.pipeline_steps.answer_beautifier import AnswerBeautifier


class BertNaturalAnswerPostprocessor(NaturalAnswerPostprocessor):

    def __init__(self):
        self.best_answer_extractor = BestAnswerExtractor()
        self.answer_beautifier = AnswerBeautifier()

    def fit(self, X: List[TextQuestionAnswerTriplet], y=None):
        return self

    def transform(self, X: List[TextQuestionAnswerTriplet], y=None) -> List[BeautifiedAnswer]:
        all_final_answers = []
        for x in X:
            final_answer = self.transform_one(x)
            all_final_answers.append(final_answer)

        return all_final_answers

    def transform_one(self, X: TextQuestionAnswerTriplet) -> BeautifiedAnswer:
        original_text, user_question, bert_answers = X
        best_answer = self.best_answer_extractor.extract_best_answer(original_text, user_question, bert_answers)
        beautified_answer = self.answer_beautifier.beautify_answer(user_question, best_answer)
        return beautified_answer
