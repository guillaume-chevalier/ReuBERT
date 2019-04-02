from typing import List

from src.domain.pipeline_steps.natural_answer_postprocessor_interface import NaturalAnswerPostprocessorInterface
from src.domain.pipeline_steps.question_answering_model_interface import TextQuestionAnswerTriplet


class BertNaturalAnswerPostprocessor(NaturalAnswerPostprocessorInterface):

    def fit(self, X: List[TextQuestionAnswerTriplet], y=None):
        # TODO: Taha.

        for original_text, user_question, bert_answers in X:
            # TODO: maybe learn some state here.
            pass

        return self

    def transform(self, X: List[TextQuestionAnswerTriplet], y=None) -> List[str]:
        # TODO: Taha.

        all_final_answers = []
        for original_text, user_question, bert_answers in X:
            # TODO: import typing and define new custom type, and ensure that the BERTModelWrapper returns this type in it's transform method..
            final_answer = self.postprocess_one_question(original_text, user_question, bert_answers)
            all_final_answers.append(final_answer)

        return all_final_answers

    def postprocess_one_question(self, original_text, user_question, bert_answers):
        return "This is my answer: {}.".format(bert_answers)
