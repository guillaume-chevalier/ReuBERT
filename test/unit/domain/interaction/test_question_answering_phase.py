import unittest

from mock import MagicMock

from src.domain.input_text.input_text_processor import InputTextProcessor
from src.domain.interaction.exit_phase import ExitPhase
from src.domain.interaction.question_answering_phase import QuestionAnsweringPhase


class TestQuestionAnsweringPhase(unittest.TestCase):

    _SOME_NON_SWITCHING_INPUT_TEXT = "some input text"
    _SOME_RESPONSE = "some response"

    def setUp(self):
        self.question_answering_phase = QuestionAnsweringPhase()
        self.input_text_processor_mock = MagicMock(spec=InputTextProcessor)

    def test__given__non_switching_input_text__when__fetching_next_interaction_phase__then__returns_itself(self):
        expected_next_phase = self.question_answering_phase

        actual_next_phase = self.question_answering_phase.fetch_next_interaction_phase(
            self._SOME_NON_SWITCHING_INPUT_TEXT
        )

        self.assertEqual(expected_next_phase, actual_next_phase)

    def test__given__switching_input_text__when__fetching_next_interaction_phase__then__returns_exit_phase(self):
        expected_next_phase = ExitPhase()

        actual_next_phase = self.question_answering_phase.fetch_next_interaction_phase(
            QuestionAnsweringPhase.SWITCHING_TO_EXIT_PHASE_MESSAGE
        )

        self.assertEqual(expected_next_phase, actual_next_phase)

    def test__when__processing_input_text__then__input_text_processor_processes_question_and_returns_appropriate_response(
        self
    ):
        expected_response = self._SOME_RESPONSE
        self.input_text_processor_mock.process_question.return_value = expected_response

        actual_response = self.question_answering_phase.process_input_text(
            self._SOME_NON_SWITCHING_INPUT_TEXT, self.input_text_processor_mock
        )

        self.input_text_processor_mock.process_question.assert_called_once_with(self._SOME_NON_SWITCHING_INPUT_TEXT)
        self.assertEqual(expected_response, actual_response)
