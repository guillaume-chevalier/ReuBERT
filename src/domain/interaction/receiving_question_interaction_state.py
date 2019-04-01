from src.domain.interaction.receiving_statement_context_interaction_state import ReceivingStatementContextInteractionState
from src.domain.interaction.interaction_state import InteractionState


class ReceivingQuestionInteractionState(InteractionState):
    SWITCHING_TO_STATEMENT_CONTEXT_PHASE_MESSAGE = "I have no more questions to ask"
    QUESTION_HAS_BEEN_WELL_RECEIVED_MESSAGE = "This is the response"

    def fetch_next_state(self, input_text):
        if input_text == self.SWITCHING_TO_STATEMENT_CONTEXT_PHASE_MESSAGE:
            return ReceivingStatementContextInteractionState()
        return self

    # TODO: pass a domain service (like InputTextProcessor) instead of the actual repository
    # TODO: change the message to the actual response
    def process_input_text(self, input_text, input_text_repository):
        #retrieve statement context from phase 1
        #Pass those is the base estimator
        #response = pipeline.transform((phase1, question))
        #input_text_repository.add_question(input_text)   give response and question in tuple
        #send response
        return self.QUESTION_HAS_BEEN_WELL_RECEIVED_MESSAGE