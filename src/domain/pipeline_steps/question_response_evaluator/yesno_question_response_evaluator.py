from src.domain.pipeline_steps.question_response_evaluator.spacy_constants import SPACY_NER


class YESNOQuestionProcessor():

    def __init__(self):
        super().__init__()

    def extract_best_answer(self, question, bert_answers):
        return bert_answers[0]

    def _determine_type_of_expected_response_from_YESNO_question(self, yes_no_question):
        return SPACY_NER.UNKNOWN.value
