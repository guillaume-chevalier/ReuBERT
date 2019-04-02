from abc import ABC

from sklearn.base import BaseEstimator, TransformerMixin


class QuestionAnsweringModelInterface(BaseEstimator, TransformerMixin, ABC):
    pass
