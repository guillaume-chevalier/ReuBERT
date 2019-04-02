from abc import ABC, abstractmethod
from typing import List, Dict, Tuple

from sklearn.base import BaseEstimator, TransformerMixin

TextQuestionAnswerTriplet = Tuple[List[str], str, Dict[float, str]]

UserInputAndQuestionTuple = Tuple[List[str], str]

# TODO Taha: maybe that the above `UserInputAndQuestionTuple` type is just like this instead, I'm not sure of what you did:
# TODO Taha:     UserInputAndQuestionTuple = Tuple[str, str]


class QuestionAnsweringModelInterface(BaseEstimator, TransformerMixin, ABC):

    @abstractmethod
    def fit(self, X: List[UserInputAndQuestionTuple]) -> 'QuestionAnsweringModelInterface':
        pass

    @abstractmethod
    def transform(self, X: List[UserInputAndQuestionTuple]) -> List[TextQuestionAnswerTriplet]:
        pass
