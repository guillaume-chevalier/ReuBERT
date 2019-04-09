from src.api.interaction.interaction_resource import InteractionResource

from src.api.response.ending_interaction_response import EndingInteractionResponse
from src.api.response.information_phase_response import InformationPhaseResponse
from src.api.response.initiating_interaction_response import InitiatingInteractionResponse
from src.api.response.question_answering_phase_response import QuestionAnsweringPhaseResponse
from src.api.response.switching_to_question_answering_phase_response import SwitchingToQuestionAnsweringPhaseResponse
from src.api.interaction.waiting_animation_thread import WaitingAnimationThread
from src.domain.interaction.interaction_phase import InteractionPhase


class InteractionResourceImpl(InteractionResource):

    def execute(self):
        do_continue = True
        InitiatingInteractionResponse().print()
        while do_continue:
            user_input = input()
            reubert_output, next_interaction_phase = self._process_user_input(user_input)
            self._process_reubert_output(reubert_output, next_interaction_phase)
            if next_interaction_phase == InteractionPhase.EXIT_PHASE:
                do_continue = False

    def _process_user_input(self, user_input):
        waiting_animation_thread = WaitingAnimationThread()
        waiting_animation_thread.start()
        reubert_output, next_interaction_phase = self.interaction_service.process_input_text(user_input)
        waiting_animation_thread.join()
        return reubert_output, next_interaction_phase

    def _process_reubert_output(self, reubert_output, next_interaction_phase):
        if next_interaction_phase == InteractionPhase.INFORMATION_PHASE:
            InformationPhaseResponse().with_output(reubert_output).print()
        elif next_interaction_phase == InteractionPhase.TRANSITION_TO_QUESTION_ANSWERING_PHASE:
            SwitchingToQuestionAnsweringPhaseResponse().with_output(reubert_output).print()
        elif next_interaction_phase == InteractionPhase.QUESTION_ANSWERING_PHASE:
            QuestionAnsweringPhaseResponse().with_output(reubert_output).print()
        elif next_interaction_phase == InteractionPhase.EXIT_PHASE:
            EndingInteractionResponse().print()
