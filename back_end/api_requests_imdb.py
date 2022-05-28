import requests
import random

# FILE NOTES: this file contains all the requests relating to the IMDB API
# API url: https://imdb-api.com/api

# Dictionary containing string format used by IMDB API to define decade and genres. These strings are the ones to
# be used to build the endpoints to make the requests.
movie_filters_api_imdb_equivalence = {"genre": ["action", "comedy", "horror", "romance", "sci_fi", "thriller,crime"],
                                      "decade": ["1970-01-01,1979-12-31",  # 70s
                                                 "1980-01-01,1989-12-31",  # 80s
                                                 "1990-01-01,1999-12-31",  # 90s
                                                 "2000-01-01,2009-12-31",  # 2000s
                                                 "2010-01-01,2019-12-31",  # 2010s
                                                 "2020-01-01,2029-12-31"]  # 2020s
                                      }  # Date format: YYYY-MM-DD  "start,end"


# endpoint_generator_api_imdb is a helper function that will "translate" the user selection of genre/decade to the
# exact string to be used for the endpoint of the IMDB API (using above defined dict movie_filters_api_equivalence
def _endpoint_generator_api_imdb(genre_selection, decade_selection):
    """Given user selection of genre and decade, returns the API endpoint string"""
    # "Translation" from the user inputs onto API decades and genres: as user selection is returned from function
    # user_input_genre_decade as a string number from 1-6, the index to be used to retrieve the string to be used for
    # the endpoint will be equivalent to the returned from user_input_genre_decade - 1. For example, if user_genre = 1
    # the user has selected "action movie" and as such the dict item will be ["genre"][0].
    endpoint_genre = movie_filters_api_imdb_equivalence["genre"][int(genre_selection) - 1]
    endpoint_decade = movie_filters_api_imdb_equivalence["decade"][int(decade_selection) - 1]

    #  Given a generic endpoint for IMDB API to access movies with ratings 7-10 by genre and decade we replace the
    #  placeholders INSERTGENRE and INSERTDECADE with the above defined endpoint_genre and endpoint_decade to build
    #  the actual endpoint to be used
    endpoint_generic = "https://imdb-api.com/API/AdvancedSearch/k_p1883gzn?title_type=feature&user_rating=7.0,10&" \
                       "release_date=INSERTDECADE&genres=INSERTGENRE&languages=en"
    endpoint_imdb = endpoint_generic.replace("INSERTGENRE", endpoint_genre).replace("INSERTDECADE", endpoint_decade)
    return endpoint_imdb


# print(_endpoint_generator_api_imdb("5", "4"))  # uncomment to test above function


# movies_selection is a helper function takes a movies_dict dictionary and a options number of options to provide
# (actually set to 6 as this is the initial number of options we will output to the user, however this can be modified
# in the future if needed) and returns a list of random indexes to be used for the movie selection.
def _random_selection(movies_dict, options=6):
    """Given a dictionary, gets the number of keys in the dict and returns a list of random indexes from that list"""
    # number of movies for the selected decade&genre within IMdB rated 7-10:
    number_movies_imdb = len(movies_dict)
    # print(f"Number of movies filtered: {number_movies_imdb}")

    random_indexes = []  # list to contain the random indexes for movie selection

    #  The below loop will generate a list of random numbers from 1 to length of the items we got back from our request
    while len(random_indexes) < options:
        # random selection of a number from 0 to numbers of results retrieved from our filtered parameters
        try:
            random_selection = random.randrange(1, number_movies_imdb)
            if random_selection not in random_indexes:  # append only if the index is unique within random_indexes
                random_indexes.append(random_selection)
        except ValueError:
            _random_selection(movies_dict, options=6)

    return random_indexes

# movies_dict = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 2}  # uncomment to view list of random indexes
# print(f"Random movie indexes: {_random_selection(movies_dict)}")  # uncomment to view list of random indexes


# movie_name_id_poster is a helper function used to standardise how we want the information from the API to be returned.
# For this we created a dictionary containing 6 keys (6 movies) with value of each key being a dictionary containing
# key:values for id, name, poster. This will allow the tittle and poster to be used as output to the user and the id to
# be used for the following API request to be done to retrieve the streaming provider.
def _movie_name_id_poster(movies_imdb_list, random_indexes_list):
    """Given a list of movies and one of random indexes, returns dictionary with movie id, name and poster"""
    # dictionary to be returned
    movies = {1: {"id": "",
                  "name": "",
                  "poster": ""},
              2: {"id": "",
                  "name": "",
                  "poster": ""},
              3: {"id": "",
                  "name": "",
                  "poster": ""},
              4: {"id": "",
                  "name": "",
                  "poster": ""},
              5: {"id": "",
                  "name": "",
                  "poster": ""},
              6: {"id": "",
                  "name": "",
                  "poster": ""}}

    for movie in movies.keys():
        # does 6 iterations (we have 6 keys) and on each iteration it will add the id, title and image
        # for every movie contained within the random movies_imdb_list
        movies[movie]["id"] = movies_imdb_list["results"][random_indexes_list[movie - 1]]["id"]
        movies[movie]["name"] = movies_imdb_list["results"][random_indexes_list[movie - 1]]["title"]
        movies[movie]["poster"] = movies_imdb_list["results"][random_indexes_list[movie - 1]]["image"]

    return movies


# EXECUTABLE FUNCTION FOR API REQUEST

def imdb_api_execution(genre, decade):
    # API endpoint for the user selection returning movies with ratings 7-10 of IMDB
    endpoint = _endpoint_generator_api_imdb(genre, decade)
    # print(endpoint)  # uncomment to check URL endpoint
    response = requests.get(endpoint)  # send the request
    # print(f"Request status code: {response.status_code}")  # uncomment to check response of our request, we got 200
    movies_imdb = response.json()  # dictionary containing movies in key "results"
    # print(movies_imdb)  # Uncomment to check the results of our query, and structure of the dict
    try:
        random_index_selection = _random_selection(movies_imdb["results"])  # creates a list of random indexes
    except TypeError:  # When max 100/day is exceeded we get TypeError
        print("Maximum of 100 daily requests exceeded.")
        return False
    # print(_movie_name_id_poster(movies_imdb, random_index_selection))  # print dictionary containing 6 random movies
    return _movie_name_id_poster(movies_imdb, random_index_selection)


# print(imdb_api_execution("5", "4"))  # uncomment to test out we ca actually retrieve 6 random movies for Scifi 2000s
