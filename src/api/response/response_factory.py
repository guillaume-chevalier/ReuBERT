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


class ResponseFactory:

    def create_from(self, reubert_output, next_interaction_phase):
        if next_interaction_phase == InteractionInitializationPhase():
            return InitiatingInteractionResponse().with_output(reubert_output)
        elif next_interaction_phase == InformationPhase():
            return InformationPhaseResponse().with_output(reubert_output)
        elif next_interaction_phase == TransitionToQuestionAnsweringPhase():
            return SwitchingToQuestionAnsweringPhaseResponse().with_output(reubert_output)
        elif next_interaction_phase == QuestionAnsweringPhase():
            return QuestionAnsweringPhaseResponse().with_output(reubert_output)
        elif next_interaction_phase == ExitPhase():
            return EndingInteractionResponse().with_output(reubert_output)