import re
from enum import Enum


class WH_CONST(Enum):
    WH_REGEX = r'who|what|how|where|when|why|which|whom|whose'
    HOW_QUANTITY_WORDS = r'far|long|many|much|old'
    OR_REGEX = r'or'
    NEGATION_REGEX = r'not|no'
    UNKNOWN_ANSWER = 'I do not know'
    YES = 'yes'
    NO = 'no'
    HOW = 'how'
    WHERE = 'where'
    WHY = 'why'
    WHAT = 'what'
    WHICH = 'which'
    WHOM = 'whom'
    WHOSE = 'whose'
    WHO = 'who'
    WHEN = 'when'


class QuestionTypeFinder:

    def __init__(self):
        pass

    def is_or_word(self, word):
        match = re.search(WH_CONST._OR_REGEX.value, word)
        if match:
            return True
        else:
            return False

    def get_wh_word_from_wh_question(self, wh_question):
        wh_match = re.search(WH_CONST.WH_REGEX.value, wh_question.lower()).group()
        return wh_match

    def contains_wh_word(self, wh_question, wh_word):
        return self.get_wh_word_from_wh_question(wh_question) == wh_word

    def contains_multiple_wh_words(self, wh_question, wh_words):
        return self.get_wh_word_from_wh_question(wh_question) in wh_words

    def find_how_quantity_word(self, wh_question):
        return re.search(WH_CONST.HOW_QUANTITY_WORDS.value, wh_question.lower()).group()

    def is_wh_question(self, question):
        match = re.search(WH_CONST.WH_REGEX.value, question)
        if match:
            return True
        else:
            return False

    def is_or_question(self, question):
        match = re.search(WH_CONST.OR_REGEX.value, question)
        if match:
            return True
        else:
            return False

    def is_yesno_question(self, question):
        return not self.is_or_question(question) and not self.is_wh_question(question)

    def is_negation_word_present(self, sentence):
        return re.search(WH_CONST.NEGATION_REGEX.value, sentence) is not None
