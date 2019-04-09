from src.api.response.response_tag import ResponseTag


class InitiatingInteractionResponse:

    def print(self):
        print(ResponseTag.GREETING_TAG.__str__(), end="\n")
        print(ResponseTag.ENTER_INFORMATION_TAG.__str__(), end="\n")
