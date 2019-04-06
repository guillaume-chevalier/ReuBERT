import re
import difflib
import en_core_web_sm

nlp = en_core_web_sm.load()


class WHQuestionResponseEvaluator:
    def __init__(self):
        super().__init__()
        self.WH_words_regex = r'who|what|how|where|when|why|which|whom|whose'
        self.HOW_quantity_words = r'far|long|many|much|old'

    def extract_best_answer(self, user_input, question, bert_answers):
        type_of_response = self._type_of_expected_response_from_WH_question(question)
        return self._verify_bert_reponses(user_input, type_of_response, bert_answers)

    def _type_of_expected_response_from_WH_question(self, wh_question):

        wh_match = re.search(self.WH_words_regex, wh_question.lower()).group()

        if wh_match == 'how':
            quantity_word = re.search(self.HOW_quantity_words, wh_question.lower()).group()
            if quantity_word:
                return ['PERCENT', 'MONEY', 'QUANTITY', 'ORDINAL', 'CARDINAL',
                        'TIME']
            else:
                return ['UNKNOWN']

        if wh_match == 'where':
            return ['LOC', 'GPE', 'ORG', 'FAC']

        if wh_match in {'why', 'what', 'which'}:
            return ['UNKNOWN']

        if wh_match in {'whom', 'whose', 'who'}:
            return ['PERSON']

        if wh_match == 'when':
            return ['DATE', 'TIME']

    def _name_sentence(self, sent):
        return [(ent.label_, ent.text) for ent in nlp(sent).ents]

    def _verify_bert_reponses(self, user_input, response_type, bert_responses):
        named_entities_from_text_by_type = self._extract_named_entities(user_input)
        for type in response_type:
            for bert_res in bert_responses:
                closest_match = self._bert_res_is_in_extracted_responses(bert_res.lower(), named_entities_from_text_by_type[type])
                if closest_match:
                    return closest_match[0]
        return bert_responses[0]

    def _extract_named_entities(self, user_input):
        full_text = ''.join(user_input)
        named_text = self._name_sentence(full_text)
        return {
            "PERCENT": self._get_named_entity_of_type('PERCENT', named_text),
            "MONEY": self._get_named_entity_of_type('MONEY', named_text),
            "QUANTITY": self._get_named_entity_of_type('QUANTITY', named_text),
            "ORDINAL": self._get_named_entity_of_type('ORDINAL', named_text),
            "CARDINAL": self._get_named_entity_of_type('CARDINAL', named_text),
            "TIME": self._get_named_entity_of_type('TIME', named_text),
            "LOC": self._get_named_entity_of_type('LOC', named_text),
            "GPE": self._get_named_entity_of_type('GPE', named_text),
            "ORG": self._get_named_entity_of_type('ORG', named_text),
            "FAC": self._get_named_entity_of_type('FAC', named_text),
            "PERSON": self._get_named_entity_of_type('PERSON', named_text),
            "DATE": self._get_named_entity_of_type('DATE', named_text),
            "UNKNOWN" : []
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

