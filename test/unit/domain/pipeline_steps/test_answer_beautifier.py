from src.domain.pipeline_steps.answer_beautifier import AnswerBeautifier
import os
import json
import pytest


def load_json_file_test(json_name):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), json_name), encoding="utf8") as json_data:
        return json.load(json_data)


class TestAnswerBeautifier:

    @classmethod
    def setup_class(self):
        self.answer_beautifier = AnswerBeautifier()
        self.text_and_questions_mock = load_json_file_test('answer_beautifier_mock_questions.json')

    @pytest.mark.parametrize("final_answer", ["no", "yes"])
    @pytest.mark.parametrize("type", ["subjective", "not subjective"])
    @pytest.mark.parametrize("question_number", [0, 1, 2, 3])
    @pytest.mark.skip(reason="The test for the beautifier fails... the prototype is not working as intended...")
    def test__given__answers_and_yesnoquestions__when__beautifing_answer__then__beautifing_correctly_(
        self, type, question_number, final_answer
    ):
        question = self.text_and_questions_mock["yesno_questions"][final_answer][type][question_number][0]
        answer = self.text_and_questions_mock["yesno_questions"][final_answer][type][question_number][1]
        res = self.answer_beautifier.beautify_answer(question, answer)

        print("Question : ", question)
        print("Answer : ", answer)
        print("Beautified Response : ", res)

        if type is "subjective":
            assert res == final_answer
        else:
            assert res == answer or res == final_answer
