from abc import ABC
from typing import List, Dict, Tuple

from sklearn.base import BaseEstimator, TransformerMixin

TextQuestionAnswerTriplet = Tuple[List[str], str, Dict[float, str]]


class QuestionAnsweringModelInterface(BaseEstimator, TransformerMixin, ABC):
    pass
