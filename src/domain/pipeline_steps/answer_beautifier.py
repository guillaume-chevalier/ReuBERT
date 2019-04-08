import re
from textblob import TextBlob


class AnswerBeautifier:
    _WH_REGEX = r'who|what|how|where|when|why|which|whom|whose'
    _HOW_QUANTITY_WORDS = r'far|long|many|much|old'
    _OR_REGEX = r'or'
    _NEGATION_REGEX = r'not|no'
    _UNKNOWN_ANSWER = 'I do not know'
    _YES = 'yes'
    _NO = 'no'

    def __init__(self):
        pass

    def beautify_answer(self, question, answer):
        if self._is_empty_answer(answer):
            return self._UNKNOWN_ANSWER

        # this step sometime fails... : It can return 'yes' when the answer is 'no' the subjectivity analysis of spacy is not perfect....
        if self._is_yesno_question(question):
            if self._is_subjective(question) or self._is_subjective(answer):
                self._handle_subjective_questions(question, answer)

            elif self._is_negation_word_present(question) or self._is_negation_word_present(answer):
                self._handle_question_with_negation_word(question, answer)

            return answer

    def _handle_subjective_questions(self, subjective_yesno_question, answer):
        if self._is_positive(subjective_yesno_question) > self._is_positive(answer) \
                or self._is_positive(subjective_yesno_question) < self._is_positive(answer):
            return self._NO

        else:
            return self._YES

    def _handle_question_with_negation_word(self, question_with_negation_word, answer):
        if self._is_negation_word_present(question_with_negation_word) != self._is_negation_word_present(answer):
            return self._NO
        else:
            return self._YES

    def _is_yesno_question(self, question):
        return not re.match(self._WH_REGEX, question.lower()) \
               and not re.match(self._OR_REGEX, question.lower())

    def _is_wh_question(self, question):
        return re.search(self._WH_REGEX, question.lower())

    def _is_empty_answer(self, answer):
        return answer == ''

    def _is_negation_word_present(self, sentence):
        return re.search(self._NEGATION_REGEX, sentence) is not None

    def _is_positive(self, sentence):
        sentiment = TextBlob(sentence).sentiment.polarity
        return sentiment

    def _is_subjective(self, sentence):
        subjectivity = TextBlob(sentence).sentiment.subjectivity
        return subjectivity > 0.0
