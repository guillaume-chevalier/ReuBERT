from textblob import TextBlob

from src.domain.pipeline_steps.question_response_evaluator.question_type_analyser import QuestionTypeFinder


class AnswerBeautifier:
    _UNKNOWN_ANSWER = 'I do not know'
    _YES = 'yes'
    _NO = 'no'

    def __init__(self):
        self.question_type_finder = QuestionTypeFinder()

    def beautify_answer(self, question, answer):
        if self._is_empty_answer(answer):
            return self._UNKNOWN_ANSWER

        # this step sometime fails... : It can return 'yes' when the answer is 'no' the subjectivity analysis of spacy is not perfect....
        if self.question_type_finder.is_yesno_question(question):
            if self._is_subjective(question) or self._is_subjective(answer):
                self._handle_subjective_questions(question, answer)

            elif self.question_type_finder.is_negation_word_present(question) \
                    or self.question_type_finder.is_negation_word_present(answer):
                self._handle_question_with_negation_word(question, answer)

        return answer

    def _handle_subjective_questions(self, subjective_yesno_question, answer):
        if self._is_positive(subjective_yesno_question) > self._is_positive(answer) \
                or self._is_positive(subjective_yesno_question) < self._is_positive(answer):
            return self._NO

        else:
            return self._YES

    def _handle_question_with_negation_word(self, question_with_negation_word, answer):
        if self.question_type_finder.is_negation_word_present(question_with_negation_word) \
                != self.question_type_finder.is_negation_word_present(answer):
            return self._NO
        else:
            return self._YES

    def _is_empty_answer(self, answer):
        return answer == ''

    def _is_positive(self, sentence):
        sentiment = TextBlob(sentence).sentiment.polarity
        return sentiment

    def _is_subjective(self, sentence):
        subjectivity = TextBlob(sentence).sentiment.subjectivity
        return subjectivity > 0.0
