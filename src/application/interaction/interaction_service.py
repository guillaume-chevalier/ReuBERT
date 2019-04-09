class InteractionService:

    def __init__(self, interaction_context, input_text_processor):
        self.interaction_context = interaction_context
        self.input_text_processor = input_text_processor

    def process_input_text(self, input_text):
        next_interaction_phase = self.interaction_context.fetch_next_interaction_phase(input_text)
        response = next_interaction_phase.process_input_text(input_text, self.input_text_processor)
        return response, next_interaction_phase
