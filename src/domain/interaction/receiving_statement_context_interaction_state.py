from src.domain.interaction.interaction_state import InteractionState


class ReceivingStatementContextInteractionState(InteractionState):
    ASKING_FOR_MORE_INFORMATION_CONTEXT_MESSAGE = "Can you give me more information please?"

    def process_input_text(self, input_text, input_text_processor):
        input_text_processor.process_context_statement(input_text)
        return self.ASKING_FOR_MORE_INFORMATION_CONTEXT_MESSAGE
