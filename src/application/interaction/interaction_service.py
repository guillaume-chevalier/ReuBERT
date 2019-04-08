class InteractionService:

    def __init__(self, interaction_state, input_text_processor):
        self.interaction_state = interaction_state
        self.input_text_processor = input_text_processor

    def process_input_text(self, input_text):
        self.interaction_state = self.interaction_state.fetch_next_state(input_text)
        return self.interaction_state.process_input_text(
            input_text, self.input_text_processor
        )
