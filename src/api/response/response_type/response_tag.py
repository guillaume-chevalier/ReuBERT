from enum import Enum


class ResponseTag(Enum):
    GREETING_TAG = (1, "ReuBERT[greeting]:~$ Welcome! What would you like to talk about?")
    GOODBYE_TAG = (2, "ReuBERT[goodbye]:~$ See you later!")
    ENTER_INFORMATION_TAG = (3, "You[enter information]:~$ ")
    GATHER_INFORMATION_TAG = (4, "ReuBERT[gather information]:~$ {}")
    ENTER_QUESTION_TAG = (5, "You[enter question]:~$ ")
    ANSWER_QUESTION_TAG = (6, "ReuBERT[answer question]:~$ {}")

    def __str__(self):
        return self.value[1]
