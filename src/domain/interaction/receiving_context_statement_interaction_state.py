from src.domain.interaction.interaction_state import InteractionState


class ReceivingContextStatementInteractionState(InteractionState):

    def process_input_text(self, input_text, input_text_processor):
        response = input_text_processor.process_context_statement(input_text)
        return response

    def __eq__(self, other):
        return isinstance(other, ReceivingContextStatementInteractionState)