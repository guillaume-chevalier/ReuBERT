from src.domain.interaction.interaction_state import InteractionState


class EndingDialogueInteractionState(InteractionState):

    EXIT_CODE = 0

    def process_input_text(self, input_text, input_text_processor):
        return self.EXIT_CODE

    def __eq__(self, other):
        return isinstance(other, EndingDialogueInteractionState)