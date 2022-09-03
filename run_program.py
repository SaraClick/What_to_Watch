from utils import providers_url
from user_input_output import (what_to_watch_tittle, user_input_genre, user_input_decade, output_movie_name_and_posters,
                               output_streaming_providers, user_input_movie, closing_message)
from api_requests_imdb import imdb_api_execution
from user_input_validation import user_input_func


def run_again(run_program_function):
    again = input("\nWould you like to search for another movie? Y or N → ")
    if again.lower() == "y":
        run_program_function()
    elif again.lower() == "n":
        closing_message()
        return False
    else:
        print("Invalid input detected, please respond 'Y' for yes or 'N' for No.")
        run_again(run_program_function)
        return


def run_program():
    what_to_watch_tittle()  # print out the title
    the_genre = user_input_func(user_input_genre)  # get user input genre and validate it
    if the_genre:  # if we have a valid genre, ask for decade input
        the_decade = user_input_func(user_input_decade)  # get user input decade and validate it
        if not the_decade:  # if no valid decade could be captured, ask if user want to run the program again
            run_again(run_program)
            return

        else:  # if we have a valid decade and genre, we execute the rest of the program

            movie_list = imdb_api_execution(the_genre, the_decade)  # generates the recommended movies list
            if not movie_list:  # If 100/daily requests exceeded, movie_list is False
                print("Try again tomorrow!")
                return
            else:
                print(f"\nHere's our recommendation for your selection:")
                output_movie_name_and_posters(movie_list)  # prints out to the user the movie recommendations
                selected_movie = user_input_func(user_input_movie)  # asks the user to select a movie from recom.
                if selected_movie:  # if the selection input is valid, print the ul streaming available
                    print(f"\nYou selected the movie {movie_list[int(selected_movie)]['name']}, "
                          f"below are the UK streaming providers:")
                    streaming = output_streaming_providers(movie_list, selected_movie, providers_url)
                    if not streaming:
                        run_again(run_program)
                        return
                else:  # if the selection made by user is not valid, as if they want to run the program again.
                    run_again(run_program)
                    return

    else:  # if no valid input has been entered by the user, ask if they want to run the program again
        run_again(run_program)
        return


if __name__ == '__main__':
    run_program()
