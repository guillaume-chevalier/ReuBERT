from src.domain.input_text.input_text_processor import InputTextProcessor


class InputTextProcessorImpl(InputTextProcessor):

    ASKING_FOR_MORE_INFORMATION_CONTEXT_MESSAGE = "Can you give me more information please?"
    EXIT_CODE = 0

    def __init__(self, input_text_repository, pipeline):
        self.input_text_repository = input_text_repository
        self.pipeline = pipeline

    def process_context_statement(self, context_statement):
        self.input_text_repository.add_context_statement(context_statement)
        return self.ASKING_FOR_MORE_INFORMATION_CONTEXT_MESSAGE

    def process_question(self, question):
        context_statements = self.input_text_repository.get_all_context_statements()
        response = self.pipeline.transform((context_statements, question))
        return response

    def process_exit_statement(self, exit_statement):
        return self.EXIT_CODE