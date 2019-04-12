import unittest

from src.api.response.response_factory import ResponseFactory
from src.api.response.response_type.ending_interaction_response import EndingInteractionResponse
from src.api.response.response_type.information_phase_response import InformationPhaseResponse
from src.api.response.response_type.initiating_interaction_response import InitiatingInteractionResponse
from src.api.response.response_type.question_answering_phase_response import QuestionAnsweringPhaseResponse
from src.api.response.response_type.switching_to_question_answering_phase_response import \
    SwitchingToQuestionAnsweringPhaseResponse
from src.domain.interaction.exit_phase import ExitPhase
from src.domain.interaction.information_phase import InformationPhase
from src.domain.interaction.interaction_initialization_phase import InteractionInitializationPhase
from src.domain.interaction.question_answering_phase import QuestionAnsweringPhase
from src.domain.interaction.transition_to_question_answering_phase import TransitionToQuestionAnsweringPhase


class TestResponseFactory(unittest.TestCase):

    _SOME_REUBERT_OUTPUT = "some reuBERT output"

    def setUp(self):
        self.response_factory = ResponseFactory()

    def test__given__interaction_initialization_phase__when__creating_response__then__returns_reuBERT_output_in_appropriate_response_format(
        self
    ):
        expected_response = InitiatingInteractionResponse().with_output(self._SOME_REUBERT_OUTPUT)

        actual_response = self.response_factory.create_from(self._SOME_REUBERT_OUTPUT, InteractionInitializationPhase())

        self.assertEqual(expected_response, actual_response)

    def test__given__information_phase__when__creating_response__then__returns_reuBERT_output_in_appropriate_response_format(
        self
    ):
        expected_response = InformationPhaseResponse().with_output(self._SOME_REUBERT_OUTPUT)

        actual_response = self.response_factory.create_from(self._SOME_REUBERT_OUTPUT, InformationPhase())

        self.assertEqual(expected_response, actual_response)

    def test__given__transition_to_question_answering_phase__when__creating_response__then__returns_reuBERT_output_in_appropriate_response_format(
        self
    ):
        expected_response = SwitchingToQuestionAnsweringPhaseResponse().with_output(self._SOME_REUBERT_OUTPUT)

        actual_response = self.response_factory.create_from(
            self._SOME_REUBERT_OUTPUT, TransitionToQuestionAnsweringPhase()
        )

        self.assertEqual(expected_response, actual_response)

    def test__given__question_answering_phase__when__creating_response__then__returns_reuBERT_output_in_appropriate_response_format(
        self
    ):
        expected_response = QuestionAnsweringPhaseResponse().with_output(self._SOME_REUBERT_OUTPUT)

        actual_response = self.response_factory.create_from(self._SOME_REUBERT_OUTPUT, QuestionAnsweringPhase())

        self.assertEqual(expected_response, actual_response)

    def test__given__exit_phase__when__creating_response__then__returns_reuBERT_output_in_appropriate_response_forma(
        self
    ):
        expected_response = EndingInteractionResponse().with_output(self._SOME_REUBERT_OUTPUT)

        actual_response = self.response_factory.create_from(self._SOME_REUBERT_OUTPUT, ExitPhase())

        self.assertEqual(expected_response, actual_response)
