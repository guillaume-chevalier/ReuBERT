from src.api.interaction.interaction_resource import InteractionResource

from src.api.interaction.waiting_animation_thread import WaitingAnimationThread
from src.domain.interaction.interaction_phase import InteractionPhase


class InteractionResourceImpl(InteractionResource):

    def __init__(self, interaction_service, response_factory):
        super().__init__(interaction_service, response_factory)
        self.do_continue = True

    def execute(self):
        self._initiate_interaction()
        while self.do_continue:
            user_input = input()
            self._process_user_input(user_input)

    def _initiate_interaction(self):
        reubert_output, next_interaction_phase = self.interaction_service.initiate_interaction()
        self.response_factory.create_from(reubert_output, next_interaction_phase).print()

    def _process_user_input(self, user_input):
        reubert_output, next_interaction_phase = self._wait_for_output(user_input)
        self.response_factory.create_from(reubert_output, next_interaction_phase).print()
        if next_interaction_phase == InteractionPhase.EXIT_PHASE:
            self.do_continue = False

    def _wait_for_output(self, user_input):
        waiting_animation_thread = self._start_waiting_animation_thread()
        reubert_output, next_interaction_phase = self.interaction_service.process_input_text(user_input)
        waiting_animation_thread.join()
        return reubert_output, next_interaction_phase

    def _start_waiting_animation_thread(self):
        waiting_animation_thread = WaitingAnimationThread()
        waiting_animation_thread.start()
        return waiting_animation_thread
