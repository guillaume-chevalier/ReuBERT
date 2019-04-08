import stringdist
import en_core_web_sm

from src.domain.pipeline_steps.question_response_evaluator.question_type_analyser import QuestionTypeFinder

nlp = en_core_web_sm.load()


class ORQuestionResponseEvaluator:
    def __init__(self):
        super().__init__()
        self.question_type_finder = QuestionTypeFinder()

    def extract_best_answer(self, or_question, bert_answers):
        ors_responses = self._determine_type_of_expected_response_from_OR_question(or_question)
        return self._verify_ors_answers(bert_answers, ors_responses)

    def _determine_type_of_expected_response_from_OR_question(self, or_question):
        tokenized_or_question = self._tokenize(or_question)
        ors = []
        for index in range(len(tokenized_or_question)):
            if self.question_type_finder.is_or_word(tokenized_or_question[index]):
                ors.append(tokenized_or_question[index - 1])
                ors.append(tokenized_or_question[index + 1])

        return ors

    def _verify_ors_answers(self, bert_answers, ors):
        acceptable_levenshtein_threshold = 0.5

        for bert_res in bert_answers:
            for or_res in ors:
                if stringdist.levenshtein(bert_res[1], or_res) / 33 < acceptable_levenshtein_threshold:
                    return bert_res

        return bert_answers[0]

    def _tokenize(self, sent):
        return nlp(sent).ents
