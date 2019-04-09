import stringdist
import difflib


class ResponseEvaluator:

    def __int__(self):
        pass

    def is_response_close_enough_using_leveinstein_with_text_separation(self, response, expected_response):
        acceptable_levenshtein_threshold = 0.5

        if len(response) < len(expected_response):
            expected_response = self._return_response_in_same_length(response, expected_response)
            for res in expected_response:
                    if stringdist.levenshtein(response, res) / 33 < acceptable_levenshtein_threshold:
                        return True

        elif len(response) > len(expected_response):
            response = self._return_response_in_same_length(expected_response, response)
            for res in response:
                    if stringdist.levenshtein(expected_response, res) / 33 < acceptable_levenshtein_threshold:
                        return True
        else:
            if stringdist.levenshtein(response, expected_response) / 33 < acceptable_levenshtein_threshold:
                return True
        return False



    def is_response_close_enough_using_difflib_with_text_separation(self, response, expected_response):
        if len(response) < len(expected_response):
            expected_response = self._return_response_in_same_length(response, expected_response)
            closest_match = difflib.get_close_matches(response, expected_response)
            if closest_match:
                    return True

        elif len(response) > len(expected_response):
            response = self._return_response_in_same_length(expected_response, response)
            closest_match = difflib.get_close_matches(expected_response, response)
            if closest_match:
                return True
        else:
            closest_match = difflib.get_close_matches(response, [expected_response])
            if closest_match:
                return True
        return False

    def is_response_close_enough_using_leveinstein(self, response, expected_response):
        acceptable_levenshtein_threshold = 0.5

        return stringdist.levenshtein(response, expected_response) / 33 < acceptable_levenshtein_threshold

    def is_response_close_enough_using_difflib(self, response, expected_response):
        closest_match = difflib.get_close_matches(response, [expected_response])
        if closest_match:
            return True
        else:
            return False

    def _return_response_in_same_length(self, response, response_to_split):
        expected_response_length = len(response.split())
        splited_response = response_to_split.split()
        possible_res = []
        for j in range(expected_response_length):
            splited_response = splited_response[j:]
            for i in range(len(splited_response) // expected_response_length):
                res = ' '.join(splited_response[i * expected_response_length:(i + 1) * expected_response_length])
                possible_res.append(res)
        return possible_res