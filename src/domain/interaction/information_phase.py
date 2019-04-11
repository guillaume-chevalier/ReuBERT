from src.domain.interaction.interaction_phase_state import InteractionPhaseState
from src.domain.interaction.transition_to_question_answering_phase import TransitionToQuestionAnsweringPhase


class InformationPhase(InteractionPhaseState):

    SWITCHING_TO_QUESTION_ANSWERING_PHASE_MESSAGE = "I am ready to ask questions."

    def fetch_next_interaction_phase(self, input_text):
        if input_text == self.SWITCHING_TO_QUESTION_ANSWERING_PHASE_MESSAGE:
            return TransitionToQuestionAnsweringPhase()
        return self

    def process_input_text(self, input_text, input_text_processor):
        return input_text_processor.process_context_statement(input_text)