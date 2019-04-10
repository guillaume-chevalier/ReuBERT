import unittest

from mock import MagicMock

from src.domain.input_text.input_text_processor import InputTextProcessor
from src.domain.interaction.interaction_phase import InteractionPhase


class TestInteractionPhase(unittest.TestCase):

    _SOME_INPUT_TEXT = "some input text"
    _SOME_RESPONSE = "some response"

    def setUp(self):
        self.input_text_processor_mock = MagicMock(spec=InputTextProcessor)

    def test__given__information_phase__when__processing_input_text__then__input_text_processor_processes_context_statement_and_returns_appropriate_response(
        self
    ):
        information_phase = InteractionPhase.INFORMATION_PHASE
        expected_response = self._SOME_RESPONSE
        self.input_text_processor_mock.process_context_statement.return_value = expected_response

        actual_response = information_phase.process_input_text(self._SOME_INPUT_TEXT, self.input_text_processor_mock)

        self.input_text_processor_mock.process_context_statement.assert_called_once_with(self._SOME_INPUT_TEXT)
        self.assertEqual(expected_response, actual_response)

    def test__given__transition_to_question_answering_phase__when__processing_input_text__then__input_text_processor_processes_phase_transition_statement_and_returns_appropriate_response(
        self
    ):
        information_phase = InteractionPhase.TRANSITION_TO_QUESTION_ANSWERING_PHASE
        expected_response = self._SOME_RESPONSE
        self.input_text_processor_mock.process_phase_transition_statement.return_value = expected_response

        actual_response = information_phase.process_input_text(self._SOME_INPUT_TEXT, self.input_text_processor_mock)

        self.input_text_processor_mock.process_phase_transition_statement.assert_called_once_with(self._SOME_INPUT_TEXT)
        self.assertEqual(expected_response, actual_response)

    def test__given__question_answering_phase__when__processing_input_text__then__input_text_processor_processes_question_and_returns_appropriate_response(
        self
    ):
        question_answering_phase = InteractionPhase.QUESTION_ANSWERING_PHASE
        expected_response = self._SOME_RESPONSE
        self.input_text_processor_mock.process_question.return_value = expected_response

        actual_response = question_answering_phase.process_input_text(
            self._SOME_INPUT_TEXT, self.input_text_processor_mock
        )

        self.input_text_processor_mock.process_question.assert_called_once_with(self._SOME_INPUT_TEXT)
        self.assertEqual(expected_response, actual_response)

    def test__given__exit_phase__when__processing_input_text__then__input_text_processor_processes_exit_statement_and_returns_appropriate_response(
        self
    ):
        exit_phase = InteractionPhase.EXIT_PHASE
        expected_response = self._SOME_RESPONSE
        self.input_text_processor_mock.process_exit_statement.return_value = expected_response

        actual_response = exit_phase.process_input_text(self._SOME_INPUT_TEXT, self.input_text_processor_mock)

        self.input_text_processor_mock.process_exit_statement.assert_called_once_with(self._SOME_INPUT_TEXT)
        self.assertEqual(expected_response, actual_response)
