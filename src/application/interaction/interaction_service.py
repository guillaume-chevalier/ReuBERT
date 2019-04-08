class InteractionService:

    def __init__(self, interaction_context, input_text_processor):
        self.interaction_context = interaction_context
        self.input_text_processor = input_text_processor

    def process_input_text(self, input_text):
        next_interaction_state = self.interaction_context.fetch_next_interaction_state(input_text)
        return next_interaction_state.process_input_text(input_text, self.input_text_processor)
