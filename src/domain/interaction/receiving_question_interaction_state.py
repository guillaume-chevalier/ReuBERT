#from src.domain.interaction.receiving_statement_context_interaction_state import \
    #ReceivingStatementContextInteractionState
from src.domain.interaction.interaction_state import InteractionState


class ReceivingQuestionInteractionState(InteractionState):
    SWITCHING_TO_STATEMENT_CONTEXT_PHASE_MESSAGE = "I have no more questions to ask"

    def fetch_next_state(self, input_text):
        if input_text == self.SWITCHING_TO_STATEMENT_CONTEXT_PHASE_MESSAGE:
            #return ReceivingStatementContextInteractionState()
            return ""
        return self

    def process_input_text(self, input_text, input_text_processor):
        response = input_text_processor.process_question(input_text)
        return response
