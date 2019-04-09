import stringdist
import difflib

class ResponseEvaluator:

    def __int__(self):
        pass

    def is_response_close_enough_using_leveinstein(self, response, expected_response):
        acceptable_levenshtein_threshold = 0.5

        return stringdist.levenshtein(response, expected_response) / 33 < acceptable_levenshtein_threshold

    def is_response_close_enough_using_difflib(self, response, expected_response):
        closest_match = difflib.get_close_matches(response, expected_response)
        if closest_match:
            return True
        else:
            return False
