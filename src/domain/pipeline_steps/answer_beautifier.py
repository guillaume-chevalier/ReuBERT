import re
from textblob import TextBlob


class AnswerBeautifier:
    def __init__(self):
        self.WH_regex = r'who|what|how|where|when|why|which|whom|whose'
        self.HOW_quantity_words = r'far|long|many|much|old'
        self.OR_regex = r'or'
        self.NEGATION_regex = r'not|no'

    def beautify_answer(self, question, answer):
        if self._is_empty_answer(answer):
            return 'I do not know'

        # this step sometime fails... : It can return 'yes' when the answer is 'no' the subjectivity analysis of spacy is not perfect....
        if self._is_yesno_question(question):
            if self._is_subjective(question) or self._is_subjective(answer):
                if self._is_positive(question) > self._is_positive(answer) \
                        or self._is_positive(question) < self._is_positive(answer):
                    return 'no'

                else:
                    return 'yes'

            elif self._is_negation_word_present(question) or self._is_negation_word_present(answer):
                if self._is_negation_word_present(question) != self._is_negation_word_present(answer):
                    return 'no'
                else:
                    return 'yes'

            return answer

        #could have added more beautifing step but for a lack of time it maybe better to realease something stable...

    def _is_yesno_question(self, question):
        return not re.match(self.WH_regex, question.lower()) \
               and not re.match(self.OR_regex, question.lower())

    def _is_wh_question(self, question):
        return re.search(self.WH_regex, question.lower())

    def _is_empty_answer(self, answer):
        return answer == ''

    def _is_negation_word_present(self, sentence):
        return re.search(self.NEGATION_regex, sentence) is not None

    def _is_positive(self, sentence):
        sentiment = TextBlob(sentence).sentiment.polarity
        return sentiment

    def _is_subjective(self, sentence):
        subjectivity = TextBlob(sentence).sentiment.subjectivity
        print(sentence, subjectivity)
        return subjectivity > 0.0
