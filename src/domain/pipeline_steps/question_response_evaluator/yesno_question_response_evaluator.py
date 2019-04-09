import copy


class YESNOQuestionProcessor():

    def __init__(self):
        super().__init__()

    def extract_best_answer(self, question, bert_answers):
        return self._extract_from_uncertain_answers(bert_answers)

    def _extract_from_uncertain_answers(self, bert_answers):
        best_answer = [0, '']
        for answer in bert_answers:
            if answer[0] > best_answer[0] and answer[1] != '':
                best_answer = copy.deepcopy(answer)
        return best_answer[1]
