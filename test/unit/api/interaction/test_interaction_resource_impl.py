import unittest

from mock import MagicMock, patch, call

from src.api.interaction.interaction_resource_impl import InteractionResourceImpl
from src.api.response.response_factory import ResponseFactory
from src.application.interaction.interaction_service import InteractionService
from src.domain.interaction.interaction_phase import InteractionPhase


class TestInteractionResourceImpl(unittest.TestCase):
    _SOME_USER_INPUTS = ["input 1", "input 2", "input 3", "input 4"]
    _SOME_REUBERT_OUTPUTS = [
        ("output 1", InteractionPhase.INFORMATION_PHASE),
        ("output 2", InteractionPhase.TRANSITION_TO_QUESTION_ANSWERING_PHASE),
        ("output 3", InteractionPhase.QUESTION_ANSWERING_PHASE), ("output 4", InteractionPhase.EXIT_PHASE)
    ]

    def setUp(self):
        self.interaction_service_mock = MagicMock(spec=InteractionService)
        self.response_factory_mock = MagicMock(spec=ResponseFactory)
        self.interaction_resource_impl = InteractionResourceImpl(
            self.interaction_service_mock, self.response_factory_mock
        )
        self.interaction_service_mock.process_input_text.side_effect = self._SOME_REUBERT_OUTPUTS

    @patch("src.api.response.response_type.initiating_interaction_response.print")
    @patch("src.api.interaction.waiting_animation_thread.Thread.join")
    @patch("src.api.interaction.waiting_animation_thread.Thread.start")
    def test__when__executing__then__waiting_animation_thread_is_started_then_terminated_each_time_user_input_is_collected(
        self, start_thread_mock, join_thread_mock, initiating_interaction_response_mock
    ):
        with patch('builtins.input', side_effect=self._SOME_USER_INPUTS):
            self.interaction_resource_impl.execute()
            self.assertEqual(start_thread_mock.call_count, len(self._SOME_USER_INPUTS))
            self.assertEqual(join_thread_mock.call_count, len(self._SOME_USER_INPUTS))

    @patch("src.api.response.response_type.initiating_interaction_response.print")
    @patch("src.api.interaction.waiting_animation_thread.Thread")
    def test__when__executing__then__interaction_service_processes_all_user_inputs_until_exit_phase_is_reached(
        self, thread_mock, initiating_interaction_response_mock
    ):
        with patch('builtins.input', side_effect=self._SOME_USER_INPUTS):
            interaction_service_calls_with_user_inputs = [
                call("input 1"), call("input 2"), call("input 3"),
                call("input 4")
            ]
            self.interaction_resource_impl.execute()

            self.interaction_service_mock.process_input_text.assert_has_calls(
                interaction_service_calls_with_user_inputs, any_order=False
            )

    @patch("src.api.response.response_type.initiating_interaction_response.print")
    @patch("src.api.interaction.waiting_animation_thread.Thread")
    def test__when__executing__then__response_factory_wraps_all_reuBERT_outputs_in_response_and_prints_them_until_exit_phase_is_reached(
        self, thread_mock, initiating_interaction_response_mock
    ):
        with patch('builtins.input', side_effect=self._SOME_USER_INPUTS):
            response_factory_calls_with_reuBERT_outputs = [
                call("output 1", InteractionPhase.INFORMATION_PHASE),
                call().print(),
                call("output 2", InteractionPhase.TRANSITION_TO_QUESTION_ANSWERING_PHASE),
                call().print(),
                call("output 3", InteractionPhase.QUESTION_ANSWERING_PHASE),
                call().print(),
                call("output 4", InteractionPhase.EXIT_PHASE),
                call().print()
            ]
            self.interaction_resource_impl.execute()

            self.response_factory_mock.create_from.assert_has_calls(
                response_factory_calls_with_reuBERT_outputs, any_order=False
            )
