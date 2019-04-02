from abc import ABC, abstractmethod

from sklearn.base import BaseEstimator, TransformerMixin


class NaturalAnswerPostprocessorInterface(BaseEstimator, TransformerMixin, ABC):

    @abstractmethod
    def fit(self, X, y=None):
        return self

    @abstractmethod
    def transform(self, X, y=None):
        new_X = X
        return new_X
