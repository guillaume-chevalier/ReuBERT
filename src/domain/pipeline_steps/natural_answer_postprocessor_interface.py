from abc import ABC

from sklearn.base import BaseEstimator, TransformerMixin


class NaturalAnswerPostprocessorInterface(BaseEstimator, TransformerMixin, ABC):
    pass
