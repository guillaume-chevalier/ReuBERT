import unittest
from mock import MagicMock

from src.domain.input_text.input_text_processor import InputTextProcessor
from src.domain.interaction.receiving_context_statement_interaction_state import \
    ReceivingContextStatementInteractionState


class TestReceivingContextStatementInteractionState(unittest.TestCase):

    _SOME_INPUT_TEXT = "some context statement"

    def setUp(self):
        self.receivingContextStatementInteractionState = ReceivingContextStatementInteractionState()
        self.input_text_processor_mock = MagicMock(spec=InputTextProcessor)

    def test__when__processing_input_text__then__input_text_processor_processes_context_statement(self):
        self.receivingContextStatementInteractionState.process_input_text(
            self._SOME_INPUT_TEXT, self.input_text_processor_mock
        )

        self.input_text_processor_mock.process_context_statement.assert_called_once_with(self._SOME_INPUT_TEXT)

    def test__when__processing_input_text__then__returns_appropriate_response(self):
        expected_response = ReceivingContextStatementInteractionState.ASKING_FOR_MORE_INFORMATION_CONTEXT_MESSAGE
        self.input_text_processor_mock.process_context_statement.return_value = expected_response

        actual_response = self.receivingContextStatementInteractionState.process_input_text(
            self._SOME_INPUT_TEXT, self.input_text_processor_mock
        )

        self.assertEqual(expected_response, actual_response)
