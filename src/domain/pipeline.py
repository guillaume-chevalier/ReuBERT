from sklearn.pipeline import Pipeline as P

from src.domain.pipeline_steps.natural_answer_postprocessor_interface import NaturalAnswerPostprocessorInterface
from src.domain.pipeline_steps.question_answering_model_interface import QuestionAnsweringModelInterface


class Pipeline(P):

    def __init__(
        self, question_answering_model: QuestionAnsweringModelInterface,
        natural_answer_postprocessor: NaturalAnswerPostprocessorInterface
    ):
        super().__init__([('qa_model', question_answering_model), ('post_processor', natural_answer_postprocessor)])
