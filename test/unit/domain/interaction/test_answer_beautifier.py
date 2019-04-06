from src.domain.pipeline_steps.answer_beautifier import AnswerBeautifier
import os
import json
import pytest


def load_json_file_test(json_name):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), json_name), encoding="utf8") as json_data:
        return json.load(json_data)


TEXT_AND_QUESTIONS_MOCK = load_json_file_test('answer_beautifier_mock_questions.json')


class TestAnswerBeautifier:
    @classmethod
    def setup_class(self):
        self.answer_beautifier = AnswerBeautifier()

    @pytest.mark.parametrize("final_answer", ["no", "yes", "I do not know"])
    @pytest.mark.parametrize("type", ["ambiguous", "not ambiguous"])
    @pytest.mark.parametrize("question_number", [0, 1, 2, 3])
    def test__given__answers_and_questions__when__beautifing_answer__then__beautifing_correctly_(self, type, question_number, final_answer):
        question = TEXT_AND_QUESTIONS_MOCK["yesno_questions"][final_answer][type][question_number][0]
        answer = TEXT_AND_QUESTIONS_MOCK["yesno_questions"][final_answer][type][question_number][1]
        res = self.answer_beautifier.beautify_answer(question, answer)
        assert res == final_answer
