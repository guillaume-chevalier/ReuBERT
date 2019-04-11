from src.domain.input_text.input_text_processor import InputTextProcessor


class InputTextProcessorImpl(InputTextProcessor):

    ASKING_FOR_MORE_INFORMATION_CONTEXT_MESSAGE = "Can you give me more information please?"
    READY_TO_ANSWER_QUESTIONS_MESSAGE = "Ok. Ask me your questions."
    EXIT_MESSAGE = "See you later!"

    def __init__(self, input_text_repository, pipeline):
        self.input_text_repository = input_text_repository
        self.pipeline = pipeline

    def process_context_statement(self, context_statement):
        self.input_text_repository.add_context_statement(context_statement)
        return self.ASKING_FOR_MORE_INFORMATION_CONTEXT_MESSAGE

    def process_phase_transition_statement(self, phase_transition_statement):
        return self.READY_TO_ANSWER_QUESTIONS_MESSAGE

    def process_question(self, question):
        context_statements = self.input_text_repository.get_all_context_statements()
        response = self.pipeline.transform_one((context_statements, question))
        return response

    def process_exit_statement(self, exit_statement):
        return self.EXIT_MESSAGE
