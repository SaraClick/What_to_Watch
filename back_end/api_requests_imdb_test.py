import unittest
import requests
from api_requests_imdb import _endpoint_generator_api_imdb, _random_selection


# NOTE: unittest are testing individually each decade and genre separately so we can ensure that the endpoints are
# being bilt correctly and also that the response code we get from our requests is 200 which means the request has
# been successful. Note that the tests can take some time (approx 30-50 sec) to complete as we are sending 12 requests.

class TestApiImdb(unittest.TestCase):
    def test_status_code_200_decade70(self):
        expected = 200
        actual = requests.get("https://imdb-api.com/API/AdvancedSearch/k_p1883gzn?title_type=feature&user_rating=7.0,10"
                              "&release_date=1970-01-01,1979-12-31&languages=en").status_code
        self.assertEqual(expected, actual)

    def test_status_code_200_decade80(self):
        expected = 200
        actual = requests.get("https://imdb-api.com/API/AdvancedSearch/k_p1883gzn?title_type=feature&user_rating=7.0,10"
                              "&release_date=1980-01-01,1989-12-31&languages=en").status_code
        self.assertEqual(expected, actual)

    def test_status_code_200_decade90(self):
        expected = 200
        actual = requests.get("https://imdb-api.com/API/AdvancedSearch/k_p1883gzn?title_type=feature&user_rating=7.0,10"
                              "&release_date=1990-01-01,1999-12-31&languages=en").status_code
        self.assertEqual(expected, actual)

    def test_status_code_200_decade2000(self):
        expected = 200
        actual = requests.get("https://imdb-api.com/API/AdvancedSearch/k_p1883gzn?title_type=feature&user_rating=7.0,10"
                              "&release_date=2000-01-01,2009-12-31&languages=en").status_code
        self.assertEqual(expected, actual)

    def test_status_code_200_decade2010(self):
        expected = 200
        actual = requests.get("https://imdb-api.com/API/AdvancedSearch/k_p1883gzn?title_type=feature&user_rating=7.0,10"
                              "&release_date=2010-01-01,2019-12-31&languages=en").status_code
        self.assertEqual(expected, actual)

    def test_status_code_200_decade2020(self):
        expected = 200
        actual = requests.get("https://imdb-api.com/API/AdvancedSearch/k_p1883gzn?title_type=feature&user_rating=7.0,10"
                              "&release_date=2020-01-01,2029-12-31&languages=en").status_code
        self.assertEqual(expected, actual)

    def test_status_code_200_genre_action(self):
        expected = 200
        actual = requests.get("https://imdb-api.com/API/AdvancedSearch/k_p1883gzn?title_type=feature&user_rating=7.0,10"
                              "&genres=action&languages=en").status_code
        self.assertEqual(expected, actual)

    def test_status_code_200_genre_comedy(self):
        expected = 200
        actual = requests.get(
            "https://imdb-api.com/API/AdvancedSearch/k_p1883gzn?title_type=feature&user_rating=7.0,10&genres=comedy&"
            "languages=en").status_code
        self.assertEqual(expected, actual)

    def test_status_code_200_genre_horror(self):
        expected = 200
        actual = requests.get(
            "https://imdb-api.com/API/AdvancedSearch/k_p1883gzn?title_type=feature&user_rating=7.0,10&genres=horror&"
            "languages=en").status_code
        self.assertEqual(expected, actual)

    def test_status_code_200_genre_romance(self):
        expected = 200
        actual = requests.get(
            "https://imdb-api.com/API/AdvancedSearch/k_p1883gzn?title_type=feature&user_rating=7.0,10&genres=romance&"
            "languages=en").status_code
        self.assertEqual(expected, actual)

    def test_status_code_200_genre_sci_fi(self):
        expected = 200
        actual = requests.get(
            "https://imdb-api.com/API/AdvancedSearch/k_p1883gzn?title_type=feature&user_rating=7.0,10&genres=sci_fi&"
            "languages=en").status_code
        self.assertEqual(expected, actual)

    def test_status_code_200_genre_thriller_crime(self):
        expected = 200
        actual = requests.get(
            "https://imdb-api.com/API/AdvancedSearch/k_p1883gzn?title_type=feature&user_rating=7.0,10&"
            "genres=thriller,crime&languages=en").status_code
        self.assertEqual(expected, actual)


class TestHelperFunctions(unittest.TestCase):
    def test_random_selection_list_len6(self):
        dict_example = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 2}
        expected = 6
        actual = len(_random_selection(dict_example))
        self.assertEqual(expected, actual)

    def test_endpoint_generator_api_imdb_2020s_sci_fi(self):
        expected = "https://imdb-api.com/API/AdvancedSearch/k_p1883gzn?title_type=feature&user_rating=7.0,10&" \
                   "release_date=2020-01-01,2029-12-31&genres=sci_fi&languages=en"
        actual = _endpoint_generator_api_imdb("5", "6")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
