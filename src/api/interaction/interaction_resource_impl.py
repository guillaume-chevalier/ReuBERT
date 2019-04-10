from src.api.interaction.interaction_resource import InteractionResource

from src.api.response.response_type.initiating_interaction_response import InitiatingInteractionResponse
from src.api.interaction.waiting_animation_thread import WaitingAnimationThread
from src.domain.interaction.interaction_phase import InteractionPhase


class InteractionResourceImpl(InteractionResource):

    def execute(self):
        do_continue = True
        InitiatingInteractionResponse().print()
        while do_continue:
            user_input = input()
            reubert_output, next_interaction_phase = self._process_user_input(user_input)
            self.response_factory.create_from(reubert_output, next_interaction_phase).print()
            if next_interaction_phase == InteractionPhase.EXIT_PHASE:
                do_continue = False

    def _process_user_input(self, user_input):
        waiting_animation_thread = WaitingAnimationThread()
        waiting_animation_thread.start()
        reubert_output, next_interaction_phase = self.interaction_service.process_input_text(user_input)
        waiting_animation_thread.join()
        return reubert_output, next_interaction_phase

