from src.api.response.response_type.ending_interaction_response import EndingInteractionResponse
from src.api.response.response_type.information_phase_response import InformationPhaseResponse
from src.api.response.response_type.question_answering_phase_response import QuestionAnsweringPhaseResponse
from src.api.response.response_type.switching_to_question_answering_phase_response import \
    SwitchingToQuestionAnsweringPhaseResponse
from src.domain.interaction.interaction_phase import InteractionPhase


class ResponseFactory:

    def create_from(self, reubert_output, next_interaction_phase):
        if next_interaction_phase == InteractionPhase.INFORMATION_PHASE:
            return InformationPhaseResponse().with_output(reubert_output)
        elif next_interaction_phase == InteractionPhase.TRANSITION_TO_QUESTION_ANSWERING_PHASE:
            return SwitchingToQuestionAnsweringPhaseResponse().with_output(reubert_output)
        elif next_interaction_phase == InteractionPhase.QUESTION_ANSWERING_PHASE:
            return QuestionAnsweringPhaseResponse().with_output(reubert_output)
        elif next_interaction_phase == InteractionPhase.EXIT_PHASE:
            return EndingInteractionResponse().with_output(reubert_output)