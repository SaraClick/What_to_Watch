import requests
from itertools import chain
from dotenv import load_dotenv
import os
load_dotenv()
APIKEY = os.getenv("APIKEY")


# FILE NOTES: this file contains all the requests from TheMovieDB API.
# API: https://www.themoviedb.org/
# API documentation: https://developers.themoviedb.org/3/getting-started/introduction
# MUST attribute the source of the data as JustWatch if website launched.


tmdb_base_url = "https://api.themoviedb.org/3"


# _tmdb_identifier_united_kingdom is a helper function used to check how tmdb API had coded United Kingdom in their
# endpoints. We needed to extract this information so we could ensure that the streaming providers obtained where unique
# for the UK.
# API documentation: https://developers.themoviedb.org/3/watch-providers/get-available-regions
def _tmdb_identifier_united_kingdom(api_key=APIKEY):
    """Access themoviedb API and returns the string code used to identify United Kingdom region for API requests"""
    uk_code = None
    generic_url = "https://api.themoviedb.org/3/watch/providers/regions?api_key=APIKEY&language=en-GB"
    endpoint = generic_url.replace("APIKEY", api_key)
    response_tmdb_regions = requests.get(endpoint)
    tmdb_regions = response_tmdb_regions.json()
    # print(tmdb_regions)  # uncomment to check out the API response info
    tmdb_regions_results = tmdb_regions["results"]
    for result in tmdb_regions_results:
        if result["english_name"] == "United Kingdom":
            uk_code = result["iso_3166_1"]
    return uk_code


# print(_tmdb_identifier_united_kingdom())  # uncomment to check the string used for UK (expected: GB)


# _streaming_providers_uk is a helper function that allowed us to obtain the name of all the streaming providers
# available on themoviedb API for UK. The list has been stored as a list on utils.py, name = providers
# API documentation :https://developers.themoviedb.org/3/watch-providers/get-movie-providers
def _streaming_providers_uk(api_key=APIKEY):
    """Requests all streaming providers for the UK, returns a list including all UK streaming providers"""
    country_code = _tmdb_identifier_united_kingdom(APIKEY)
    generic_url = "https://api.themoviedb.org/3/watch/providers/movie?api_key=APIKEY&language=en-US&" \
                  "watch_region=COUNTRYCODE"
    endpoint = generic_url.replace("COUNTRYCODE", country_code.replace("APIKEY", api_key)).replace("APIKEY", api_key)
    response_tmdb_streaming_providers = requests.get(endpoint)
    tmdb_providers = response_tmdb_streaming_providers.json()
    # print(tmdb_providers)  # uncomment to check the info returned from api request
    tmdb_providers_results = tmdb_providers["results"]
    providers_uk = []  # empty list to add the names of all providers available in the UK (GB code)
    for provider in tmdb_providers_results:
        provider_name = provider["provider_name"]
        if provider_name not in providers_uk:
            providers_uk.append(provider_name)
        else:
            continue
    return sorted(providers_uk)


# print(_streaming_providers_uk())  # uncomment to test _streaming_providers_uk


# _convert_imdb_to_tmdb_id is a helper function that converts an IMDB id onto a TMDB id. This function is needed
# because themoviedb API uses its own ids and doesn't allow to directly search using IMDB ids. However, themoviedb API
# has an option to convert from externals ids such as IMDB onto its own ids, which is what we did with this function.
# API documentation for find: https://developers.themoviedb.org/3/find/find-by-id
def _convert_imdb_to_tmdb_id(imdb_id, api_key=APIKEY, base_url="https://api.themoviedb.org/3"):
    """Given api_key and Imdb ID, builds specific endpoint, sends requests to tmdb and returns themoviedb ID"""
    generic_url = "/find/IMDBID?api_key=APIKEY&language=en-US&external_source=imdb_id"
    endpoint = base_url + generic_url.replace("APIKEY", api_key).replace("IMDBID", str(imdb_id))
    response_imdb_to_tmdb_id = requests.get(endpoint)
    tmdb_data = response_imdb_to_tmdb_id.json()
    # print(tmdb_data)  # uncomment to checkout tmdb_data
    tmdb_id = tmdb_data["movie_results"][0]["id"]  # gets the tmdb ID
    return tmdb_id


# print(_convert_imdb_to_tmdb_id("tt0120338"))  # uncomment to check _convert_imdb_to_tmdb_id for titanic
# should print 597


# _uk_movie_provider is a helper function that will retrieve from themoviedb API all the UK providers for a specific
# movie. Note that this return will contain all the providers including the ones that we are not targeting for our
# program. The selection from within these providers is made with a different function we have in utils named
# provider_names_to_user
# API documentation: https://developers.themoviedb.org/3/movies/get-movie-details
def uk_movie_provider(tmdb_id, api_key=APIKEY, base_url="https://api.themoviedb.org/3"):
    """Given an TMDB id, it returns a list containing all providers for streaming in the UK"""
    movie_providers = []
    uk_code = _tmdb_identifier_united_kingdom(api_key)

    generic_url = "/movie/TMDBID/watch/providers?api_key=APIKEY"
    endpoint = base_url + generic_url.replace("APIKEY", api_key).replace("TMDBID", str(tmdb_id))
    response_tmdb_provider = requests.get(endpoint)
    movie_provider = response_tmdb_provider.json()
    # print(movie_provider)  # uncomment to check what is returned

    try:
        membership_provider = movie_provider["results"][uk_code]["flatrate"]  # movie membership providers info
        rent_provider = movie_provider["results"][uk_code]["rent"]  # movie rental providers info
        buy_provider = movie_provider["results"][uk_code]["buy"]  # movie buy providers info
    except KeyError:
        return False

    else:
        for provider in list(chain(membership_provider, rent_provider, buy_provider)):
            # using itertools chain() to search on all lists at once
            if provider in movie_providers:
                continue
            else:
                movie_providers.append(provider["provider_name"])
        return movie_providers


# print(uk_movie_provider(597))  # uncomment to test _uk_movie_provider for Titanic
# print(uk_movie_provider(181812))  # uncomment to test _uk_movie_provider for Star Wars episode IX
