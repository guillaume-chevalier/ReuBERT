import unittest

from src.domain.interaction.interaction_context import InteractionContext
from src.domain.interaction.interaction_phase import InteractionPhase


class TestInteractionContext(unittest.TestCase):

    _SOME_NON_SWITCHING_INPUT_TEXT = "input text"

    def setUp(self):
        self.interaction_context = InteractionContext()

    def test__when__instantiating_interaction_context__then__has_information_phase_as_initial_interaction_phase(self):
        actual_initial_interaction_phase = self.interaction_context.current_interaction_phase

        self.assertEqual(InteractionPhase.INFORMATION_PHASE, actual_initial_interaction_phase)

    def test__given__non_switching_input_text_in_information_phase__when__fetching_next_interaction_phase__then__returns_information_phase(
        self
    ):
        expected_next_interaction_phase = InteractionPhase.INFORMATION_PHASE
        self.interaction_context.current_interaction_phase = InteractionPhase.INFORMATION_PHASE

        actual_next_interaction_phase = self.interaction_context.fetch_next_interaction_phase(
            self._SOME_NON_SWITCHING_INPUT_TEXT
        )

        self.assertEqual(expected_next_interaction_phase, actual_next_interaction_phase)

    def test__given__switching_input_text_to_question_answering_phase_in_information_phase__when__fetching_next_interaction_phase__then__returns_transition_to_question_answering_phase(
        self
    ):
        expected_next_interaction_phase = InteractionPhase.TRANSITION_TO_QUESTION_ANSWERING_PHASE
        self.interaction_context.current_interaction_phase = InteractionPhase.INFORMATION_PHASE

        actual_next_interaction_phase = self.interaction_context.fetch_next_interaction_phase(
            InteractionContext.SWITCHING_TO_QUESTION_ANSWERING_PHASE_MESSAGE
        )

        self.assertEqual(expected_next_interaction_phase, actual_next_interaction_phase)

    def test__given__non_switching_input_text_in_transition_to_question_answering_phase__when__fetching_next_interaction_phase__then__returns_question_answering_phase(
        self
    ):
        expected_next_interaction_phase = InteractionPhase.QUESTION_ANSWERING_PHASE
        self.interaction_context.current_interaction_phase = InteractionPhase.TRANSITION_TO_QUESTION_ANSWERING_PHASE

        actual_next_interaction_phase = self.interaction_context.fetch_next_interaction_phase(
            self._SOME_NON_SWITCHING_INPUT_TEXT
        )

        self.assertEqual(expected_next_interaction_phase, actual_next_interaction_phase)

    def test__given__switching_input_text_to_exit_phase_in_transition_to_question_answering_phase__when__fetching_next_interaction_phase__then__returns_exit_phase(
        self
    ):
        expected_next_interaction_phase = InteractionPhase.EXIT_PHASE
        self.interaction_context.current_interaction_phase = InteractionPhase.TRANSITION_TO_QUESTION_ANSWERING_PHASE

        actual_next_interaction_phase = self.interaction_context.fetch_next_interaction_phase(
            InteractionContext.SWITCHING_TO_EXIT_PHASE_MESSAGE
        )

        self.assertEqual(expected_next_interaction_phase, actual_next_interaction_phase)

    def test__given__non_switching_input_text_in_question_answering_phase__when__fetching_next_interaction_phase__then__returns_question_answering_phase(
        self
    ):
        expected_next_interaction_phase = InteractionPhase.QUESTION_ANSWERING_PHASE
        self.interaction_context.current_interaction_phase = InteractionPhase.QUESTION_ANSWERING_PHASE

        actual_next_interaction_phase = self.interaction_context.fetch_next_interaction_phase(
            self._SOME_NON_SWITCHING_INPUT_TEXT
        )

        self.assertEqual(expected_next_interaction_phase, actual_next_interaction_phase)

    def test__given__switching_input_text_to_exit_phase_in_question_answering_phase__when__fetching_next_interaction_phase__then__returns_exit_phase(
        self
    ):
        expected_next_interaction_phase = InteractionPhase.EXIT_PHASE
        self.interaction_context.current_interaction_phase = InteractionPhase.QUESTION_ANSWERING_PHASE

        actual_next_interaction_phase = self.interaction_context.fetch_next_interaction_phase(
            InteractionContext.SWITCHING_TO_EXIT_PHASE_MESSAGE
        )

        self.assertEqual(expected_next_interaction_phase, actual_next_interaction_phase)
