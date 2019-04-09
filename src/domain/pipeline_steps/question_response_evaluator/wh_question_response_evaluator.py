import difflib
import en_core_web_sm
import copy

from src.domain.pipeline_steps.question_response_evaluator.question_type_analyser import QuestionTypeFinder, WH_CONST
from src.domain.pipeline_steps.question_response_evaluator.spacy_constants import SPACY_NER

nlp = en_core_web_sm.load()


class WHQuestionResponseEvaluator:
    _QUANTITY_CONST = [SPACY_NER.PERCENT.value, SPACY_NER.MONEY.value, SPACY_NER.QUANTITY.value,
                       SPACY_NER.ORDINAL.value,
                       SPACY_NER.CARDINAL.value, SPACY_NER.TIME.value]
    _UNKNOWN_CONST = [SPACY_NER.UNKNOWN.value]
    _LOCATION_CONST = [SPACY_NER.LOC.value, SPACY_NER.GPE.value, SPACY_NER.ORG.value, SPACY_NER.FAC.value]
    _PERSON_CONST = [SPACY_NER.PERSON.value]
    _TIME_CONST = [SPACY_NER.DATE.value, SPACY_NER.TIME.value]

    def __init__(self):
        super().__init__()
        self.question_type_finder = QuestionTypeFinder()

    def extract_best_answer(self, user_input, question, bert_answers):
        type_of_response = self._type_of_expected_response_from_WH_question(question)
        extract_ans = self._extract_wh_matching_answer(user_input, type_of_response, bert_answers)
        if extract_ans:
            return extract_ans
        else:
            return self._extract_from_uncertain_answers(bert_answers)

    def _extract_from_uncertain_answers(self, bert_answers):
        best_answer = [0, '']
        for answer in bert_answers:
            if answer[0] > best_answer[0] and answer[1] != '':
                best_answer = copy.deepcopy(answer)
        return best_answer[1]

    def _type_of_expected_response_from_WH_question(self, wh_question):

        if self.question_type_finder.contains_wh_word(wh_question, WH_CONST.HOW.value):
            how_quantity_word = self.question_type_finder.find_how_quantity_word(wh_question)
            if how_quantity_word:
                return self._QUANTITY_CONST
            else:
                return self._UNKNOWN_CONST

        if self.question_type_finder.contains_wh_word(wh_question, WH_CONST.WHERE.value):
            return self._LOCATION_CONST

        if self.question_type_finder.contains_multiple_wh_words(wh_question, {WH_CONST.WHY.value, WH_CONST.WHAT.value,
                                                                              WH_CONST.WHICH.value}):
            return self._UNKNOWN_CONST

        if self.question_type_finder.contains_multiple_wh_words(wh_question, {WH_CONST.WHOM.value, WH_CONST.WHOSE.value,
                                                                              WH_CONST.WHO.value}):
            return self._PERSON_CONST

        if self.question_type_finder.contains_wh_word(wh_question, WH_CONST.WHEN.value):
            return self._TIME_CONST

    def _name_sentence(self, sent):
        return [(ent.label_, ent.text) for ent in nlp(sent).ents]

    def _extract_wh_matching_answer(self, user_input, response_type, bert_responses):
        bert_responses = self._extract_responses_only(bert_responses)
        named_entities_from_text_by_type = self._extract_named_entities(user_input)
        for type in response_type:
            for bert_res in bert_responses:
                closest_match = self._bert_res_is_in_extracted_responses(bert_res.lower(),
                                                                         named_entities_from_text_by_type[type])
                if closest_match:
                    return closest_match[0]

    def _extract_named_entities(self, user_input):
        full_text = ''.join(user_input)
        named_text = self._name_sentence(full_text)
        return {
            SPACY_NER.PERCENT.value: self._get_named_entity_of_type(SPACY_NER.PERCENT.value, named_text),
            SPACY_NER.MONEY.value: self._get_named_entity_of_type(SPACY_NER.MONEY.value, named_text),
            SPACY_NER.QUANTITY.value: self._get_named_entity_of_type(SPACY_NER.QUANTITY.value, named_text),
            SPACY_NER.ORDINAL.value: self._get_named_entity_of_type(SPACY_NER.ORDINAL.value, named_text),
            SPACY_NER.CARDINAL.value: self._get_named_entity_of_type(SPACY_NER.CARDINAL.value, named_text),
            SPACY_NER.TIME.value: self._get_named_entity_of_type(SPACY_NER.TIME.value, named_text),
            SPACY_NER.LOC.value: self._get_named_entity_of_type(SPACY_NER.LOC.value, named_text),
            SPACY_NER.GPE.value: self._get_named_entity_of_type(SPACY_NER.GPE.value, named_text),
            SPACY_NER.ORG.value: self._get_named_entity_of_type(SPACY_NER.ORG.value, named_text),
            SPACY_NER.FAC.value: self._get_named_entity_of_type(SPACY_NER.FAC.value, named_text),
            SPACY_NER.PERSON.value: self._get_named_entity_of_type(SPACY_NER.PERSON.value, named_text),
            SPACY_NER.DATE.value: self._get_named_entity_of_type(SPACY_NER.DATE.value, named_text),
            SPACY_NER.UNKNOWN.value: []
        }

    def _get_named_entity_of_type(self, type, named_text):
        result = []
        for item in named_text:
            if item[0] == type:
                result.append(item[1].lower())
        return result

    def _bert_res_is_in_extracted_responses(self, bert_res, extracted_res):
        closest_match = difflib.get_close_matches(bert_res, extracted_res)
        return closest_match

    def _extract_responses_only(self, bert_response):
        return [answer[1] for answer in bert_response]
