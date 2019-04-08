from src.domain.interaction.interaction_state import InteractionState


class ReceivingQuestionInteractionState(InteractionState):

    def process_input_text(self, input_text, input_text_processor):
        response = input_text_processor.process_question(input_text)
        return response
