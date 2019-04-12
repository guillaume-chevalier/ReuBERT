from src.domain.interaction.interaction_initialization_phase import InteractionInitializationPhase


class InteractionService:

    def __init__(self, input_text_processor):
        self.interaction_phase = InteractionInitializationPhase()
        self.input_text_processor = input_text_processor

    def initiate_interaction(self):
        response = self.interaction_phase.process_input_text("", self.input_text_processor)
        return response, self.interaction_phase

    def process_input_text(self, input_text):
        next_interaction_phase = self.interaction_phase.fetch_next_interaction_phase(input_text)
        response = next_interaction_phase.process_input_text(input_text, self.input_text_processor)
        self.interaction_phase = next_interaction_phase
        return response, next_interaction_phase
