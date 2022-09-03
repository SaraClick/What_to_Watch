import unittest
import requests
from api_requests_streaming import _convert_imdb_to_tmdb_id, uk_movie_provider, _tmdb_identifier_united_kingdom
from utils import provider_names_to_user, providers
from dotenv import load_dotenv
import os
load_dotenv()
APIKEY = os.getenv("APIKEY")


class TestStreamingProvidersUK(unittest.TestCase):
    def test_endpoint_streaming_providers_uk(self):
        # Check that the request ger code is 200 → no issues with the request
        expected = 200
        endpoint = "https://api.themoviedb.org/3/watch/providers/movie?api_key=APIKEY&language=en-US&watch_region=GB"\
            .replace("APIKEY", APIKEY)
        actual = requests.get(endpoint).status_code
        self.assertEqual(expected, actual)


class TestScreeningApi(unittest.TestCase):
    def test_endpoint_convert_imdb_to_tmdb_id_Titanic(self):
        endpoint = "https://api.themoviedb.org/3/find/IMDBID?api_key=APIKEY&language=en-US&external_source=imdb_id".\
            replace("APIKEY", APIKEY).replace("IMDBID", "tt0120338")
        expect = 200
        actual = requests.get(endpoint).status_code
        self.assertEqual(expect, actual)

    def test_endpoint_convert_imdb_to_tmdb_id_DontLookUp(self):
        endpoint = "https://api.themoviedb.org/3/find/IMDBID?api_key=APIKEY&language=en-US&external_source=imdb_id".\
            replace("APIKEY", APIKEY).replace("IMDBID", "tt0120338")
        expect = 200
        actual = requests.get(endpoint).status_code
        self.assertEqual(expect, actual)

    def test_convert_imdb_to_tmdb_id_titanic(self):
        expect = 597  # themovieDB id for Titanic
        actual = _convert_imdb_to_tmdb_id("tt0120338")
        self.assertEqual(expect, actual)

    def test_convert_imdb_to_tmdb_id_star_wars_ix(self):
        expect = 181812  # themovieDB id for Star Wars: Episode IX - The Rise of Skywalker
        actual = _convert_imdb_to_tmdb_id("tt2527338")
        self.assertEqual(expect, actual)

    def test_uk_movie_provider_titanic(self):
        # NOTE: if this test fails could be due to provider availability changes, provides as checked May 2022
        expect = sorted(['Virgin TV Go', 'Apple iTunes', 'Google Play Movies', 'Rakuten TV', 'Sky Store', 'Chili',
                         'Amazon Video', 'YouTube', 'Microsoft Store', 'Apple iTunes', 'Google Play Movies',
                         'Sky Store', 'Rakuten TV', 'Chili', 'Amazon Video', 'YouTube', 'Microsoft Store'])
        actual = sorted(uk_movie_provider(597))
        self.assertEqual(expect, actual)

    def test_uk_movie_provider_star_wars_ix(self):
        # NOTE: if this test fails could be due to provider availability changes, provides as checked May 2022
        expect = sorted(['Disney Plus', 'Virgin TV Go', 'Google Play Movies', 'YouTube', 'Apple iTunes', 'Rakuten TV',
                         'Sky Store', 'Chili', 'Amazon Video', 'Microsoft Store'])
        actual = sorted(uk_movie_provider(181812))
        self.assertEqual(expect, actual)


class TestTmdbIdentifierUK(unittest.TestCase):
    def test_endpoint_tmdb_idetifier_united_kingdom(self):
        # Check that the request ger code is 200 → no issues with the request
        expected = 200
        endpoint = "https://api.themoviedb.org/3/watch/providers/regions?api_key=APIKEY&language=en-GB".replace(
            "APIKEY", APIKEY)
        actual = requests.get(endpoint).status_code
        self.assertEqual(expected, actual)

    def test_UK_as_GB(self):
        # Hard coded "GB" used in api_requests_steaming to avoid a request for every time we use it
        # also this info has very low risk to change in the API
        expected = "GB"
        actual = _tmdb_identifier_united_kingdom(APIKEY)
        self.assertEqual(expected, actual)


class TestProviderNameToUser(unittest.TestCase):
    def test_streaming_providers_uk_all6(self):
        # Check that all providers used in our program are indeed UK providers
        expected = {"Amazon", "Apple", "BBC", "Disney", "Netflix", "Sky"}
        actual = provider_names_to_user(providers)
        self.assertEqual(expected, actual)

    def test_streaming_providers_uk_none_of_6(self):
        # Check that all providers used in our program are indeed UK providers
        expected = "No UK streaming availability for Amazon, Apple, BBC, Disney, Netflix or Sky"
        actual = provider_names_to_user("HBO")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
