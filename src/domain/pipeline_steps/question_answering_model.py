from abc import ABC, abstractmethod
from typing import List, Dict, Tuple

from sklearn.base import BaseEstimator, TransformerMixin

TextQuestionAnswerTriplet = List[Tuple[float, str]]

UserInputAndQuestionTuple = Dict[List[str], str]


class QuestionAnsweringModel(BaseEstimator, TransformerMixin, ABC):

    @abstractmethod
    def fit(self, X: List[UserInputAndQuestionTuple]) -> 'QuestionAnsweringModel':
        pass

    @abstractmethod
    def transform(self, X: List[UserInputAndQuestionTuple]) -> List[TextQuestionAnswerTriplet]:
        pass
