from src.api.response.response import Response
from src.api.response.response_tag import ResponseTag


class InitiatingInteractionResponse(Response):

    def print(self):
        print(ResponseTag.GREETING_TAG.__str__() + "\n" + ResponseTag.ENTER_INFORMATION_TAG.__str__() + "\n")
