class InteractionService:

    # TODO: pass a context instead of an interaction_state. The context will keep track of the actual state, not the service
    def __init__(self, input_text_repository, interaction_state, bert_model_wrapper):
        self.input_text_repository = input_text_repository
        self.interaction_state = interaction_state
        self.bert_model_wrapper = bert_model_wrapper

    def process_input_text(self, input_text):
        self.interaction_state = self.interaction_state.fetch_next_state(input_text)
        return self.interaction_state.process_input_text(
            input_text, self.input_text_repository, self.bert_model_wrapper
        )
