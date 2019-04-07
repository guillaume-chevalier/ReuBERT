from abc import ABC, abstractmethod
from typing import List, Dict, Tuple

from sklearn.base import BaseEstimator, TransformerMixin

TextQuestionAnswerTriplet = Tuple[str, str, List[Tuple[float, str]]]

UserInputAndQuestionTuple = Tuple[List[str], str]

BeautifiedAnswer = str


class QuestionAnsweringModel(BaseEstimator, TransformerMixin, ABC):

    @abstractmethod
    def fit(self, X: List[UserInputAndQuestionTuple]) -> 'QuestionAnsweringModel':
        pass

    @abstractmethod
    def transform(self, X: List[UserInputAndQuestionTuple]) -> List[TextQuestionAnswerTriplet]:
        pass
