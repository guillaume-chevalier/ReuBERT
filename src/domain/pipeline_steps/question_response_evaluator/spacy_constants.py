from enum import Enum

class SPACY_NER(Enum):
    PERCENT = 'PERCENT'
    PERSON = 'PERSON'
    MONEY = 'MONEY'
    QUANTITY = 'QUANTITY'
    ORDINAL = 'ORDINAL'
    CARDINAL = 'CARDINAL'
    TIME = 'TIME'
    UNKNOWN = 'UNKNOWN'
    LOC = 'LOC'
    GPE = 'GPE'
    ORG = 'ORG'
    FAC = 'FAC'
    DATE = 'DATE'