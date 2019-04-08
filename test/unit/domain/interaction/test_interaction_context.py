import unittest

from src.domain.interaction.ending_dialogue_interaction_state import EndingDialogueInteractionState
from src.domain.interaction.interaction_context import InteractionContext
from src.domain.interaction.receiving_context_statement_interaction_state import \
    ReceivingContextStatementInteractionState
from src.domain.interaction.receiving_question_interaction_state import ReceivingQuestionInteractionState


class TestInteractionContext(unittest.TestCase):

    _SOME_NON_SWITCHING_INPUT_TEXT = "input text"

    def setUp(self):
        self.interaction_context = InteractionContext()

    def test__when__instantiating_interaction_context__then__has_context_statement_interaction_state_as_initial_state(
        self
    ):
        actual_initial_state = self.interaction_context.interaction_state

        self.assertEqual(ReceivingContextStatementInteractionState(), actual_initial_state)

    def test__given__non_switching_input_text__when__fetching_next_interaction_state__then__returns_current_interaction_state(
        self
    ):
        expected_next_interaction_state = self.interaction_context.interaction_state

        actual_next_interaction_state = self.interaction_context.fetch_next_interaction_state(
            self._SOME_NON_SWITCHING_INPUT_TEXT
        )

        self.assertEqual(expected_next_interaction_state, actual_next_interaction_state)

    def test__given__switching_input_text_to_question_interaction_state__when__fetching_next_interaction_state__then__returns_question_interaction_state(
            self
    ):
        expected_next_interaction_state = ReceivingQuestionInteractionState()

        actual_next_interaction_state = self.interaction_context.fetch_next_interaction_state(
            InteractionContext.SWITCHING_TO_QUESTION_ANSWERING_PHASE_MESSAGE
        )

        self.assertEqual(expected_next_interaction_state, actual_next_interaction_state)

    def test__given__switching_input_text_to_ending_dialogue_interaction_state__when__fetching_next_interaction_state__then__returns_ending_dialogue_interaction_state(
        self
    ):
        expected_next_interaction_state = EndingDialogueInteractionState()

        actual_next_interaction_state = self.interaction_context.fetch_next_interaction_state(
            InteractionContext.SWITCHING_TO_INTERACTION_ENDING_PHASE_MESSAGE
        )

        self.assertEqual(expected_next_interaction_state, actual_next_interaction_state)


