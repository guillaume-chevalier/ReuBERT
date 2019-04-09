from src.api.response.response_tag import ResponseTag


class EndingInteractionResponse:

    def print(self):
        print("\n" + ResponseTag.GOODBYE_TAG.__str__(), end="\n")