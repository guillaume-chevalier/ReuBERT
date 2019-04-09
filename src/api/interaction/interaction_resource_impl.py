from src.api.interaction.interaction_resource import InteractionResource

from src.api.response.ending_interaction_response import EndingInteractionResponse
from src.api.response.information_phase_response import InformationPhaseResponse
from src.api.response.initiating_interaction_response import InitiatingInteractionResponse
from src.api.response.question_answering_phase_response import QuestionAnsweringPhaseResponse
from src.api.response.switching_to_question_answering_phase_response import SwitchingToQuestionAnsweringPhaseResponse
from src.domain.interaction.interaction_phase import InteractionPhase


class InteractionResourceImpl(InteractionResource):

    def execute(self):
        do_continue = True

        print(InitiatingInteractionResponse())
        while do_continue:
            user_input = input()
            reubert_output, next_interaction_phase = self.interaction_service.process_input_text(user_input)
            if next_interaction_phase == InteractionPhase.INFORMATION_PHASE:
                print(InformationPhaseResponse().with_output(reubert_output))
            elif next_interaction_phase == InteractionPhase.TRANSITION_TO_QUESTION_ANSWERING_PHASE:
                print(SwitchingToQuestionAnsweringPhaseResponse().with_output(reubert_output))
            elif next_interaction_phase == InteractionPhase.QUESTION_ANSWERING_PHASE:
                print(QuestionAnsweringPhaseResponse().with_output(reubert_output))
            elif next_interaction_phase == InteractionPhase.EXIT_PHASE:
                print(EndingInteractionResponse())
                do_continue = False

