from src.api.response.response_type.response_tag import ResponseTag


class EndingInteractionResponse:

    def print(self):
        print("\n" + ResponseTag.GOODBYE_TAG.__str__(), end="\n")

    def __eq__(self, other):
        return isinstance(other, self.__class__)
