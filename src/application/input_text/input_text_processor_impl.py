from src.domain.input_text.input_text_processor import InputTextProcessor


class InputTextProcessorImpl(InputTextProcessor):

    def __init__(self, input_text_repository, pipeline):
        self.input_text_repository = input_text_repository
        self.pipeline = pipeline

    def process_context_statement(self, context_statement, pipeline):
        self.input_text_repository.add_context_statement(context_statement)

    def process_question(self, question, pipeline):
        context_statements = self.input_text_repository.get_all_context_statements()
        response = pipeline.transform((context_statements, question))
        return response