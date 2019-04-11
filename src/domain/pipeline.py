from sklearn.pipeline import Pipeline as P

from src.domain.pipeline_steps.natural_answer_postprocessor import NaturalAnswerPostprocessor
from src.domain.pipeline_steps.question_answering_model import QuestionAnsweringModel


class Pipeline(P):

    def __init__(
        self, question_answering_model: QuestionAnsweringModel, natural_answer_postprocessor: NaturalAnswerPostprocessor
    ):
        super().__init__([('qa_model', question_answering_model), ('post_processor', natural_answer_postprocessor)])

    def transform_one(self, X):
        return self.transform([X])[0]
