import unittest

from mock import MagicMock

from src.domain.input_text.input_text_processor import InputTextProcessor
from src.domain.interaction.exit_phase import ExitPhase


class TestExitPhase(unittest.TestCase):

    _SOME_INPUT_TEXT = "some input text"
    _SOME_RESPONSE = "some response"

    def setUp(self):
        self.exit_phase = ExitPhase()
        self.input_text_processor_mock = MagicMock(spec=InputTextProcessor)

    def test__when__fetching_next_interaction_phase__then__returns_itself(self):
        expected_next_phase = self.exit_phase

        actual_next_phase = self.exit_phase.fetch_next_interaction_phase(self._SOME_INPUT_TEXT)

        self.assertEqual(expected_next_phase, actual_next_phase)

    def test__when__processing_input_text__then__input_text_processor_processes_exit_statement_and_returns_appropriate_response(
        self
    ):
        expected_response = self._SOME_RESPONSE
        self.input_text_processor_mock.process_exit_statement.return_value = expected_response

        actual_response = self.exit_phase.process_input_text(self._SOME_INPUT_TEXT, self.input_text_processor_mock)

        self.input_text_processor_mock.process_exit_statement.assert_called_once_with(self._SOME_INPUT_TEXT)
        self.assertEqual(expected_response, actual_response)
