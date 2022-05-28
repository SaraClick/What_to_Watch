from utils import provider_names_to_user, decorator_stars, decorator_empty_line, decorator_underscore
from api_requests_streaming import uk_movie_provider

# User inputs used in api_requests_imdb  for testing of the API requests


@decorator_empty_line
@decorator_stars
def what_to_watch_tittle():
    print("WHAT TO WATCH")


#  function used un run_program file to ask the user for their input for genre
def user_input_genre():
    """Prompts the user to enter a number from 1-6 to select genre and then select decade. Returns genre, decade"""
    user_genre = input("Select a genre from the below:"
                       "\n1: Action"
                       "\n2: Comedy"
                       "\n3: Horror"
                       "\n4: Romance"
                       "\n5: SciFi"
                       "\n6: Thriller&Crime"
                       "\nEnter here the option number → ")
    return user_genre


#  function used un run_program file to ask the user for their input for decade
def user_input_decade():
    user_decade = input("\nSelect a decade from the below:"
                        "\n1: 70s"
                        "\n2: 80s"
                        "\n3: 90s"
                        "\n4: 2000"
                        "\n5: 2010"
                        "\n6: 2020"
                        "\nEnter here the option number → ")
    return user_decade


#  function used un run_program file to ask the user for their input for one of the 6 movie recommendation
def user_input_movie():
    user_movie = input("\nEnter here the number of the movie you would like to watch → ")
    return user_movie


#  function used un run_program file to show the user the random movie selection made with link to its poster
def output_movie_name_and_posters(movies_dict):
    """Given a dictionary of movies and posters, prints out the movie and link to poster"""
    for movie, info in movies_dict.items():
        print(f"{movie}: {info['name']}  |  Poster: {info['poster']}")
    return


#  function used un run_program file to show the available provider options with the link to the site
def output_streaming_providers(movies, user_movie_selection, providers_url_dict):
    streaming_availability = uk_movie_provider(movies[int(user_movie_selection)]['id'])

    if streaming_availability:
        streaming_selection = provider_names_to_user(streaming_availability)
        for idx, provider in enumerate(streaming_selection):
            print(f"{idx + 1}: {provider}  |  Web: {providers_url_dict[provider]}")

    else:
        print("Sorry, there is no availability in the UK for Amazon, Apple TV, BBC, Disney+ nor Netflix.")
        return


@decorator_empty_line
@decorator_underscore
def closing_message():
    print("Thanks for using What To Watch, we will keep the popcorn ready for next time!"
          "\n***THE END***")


if __name__ == '__main__':
    what_to_watch_tittle()
    user_input_genre()
    user_input_decade()
