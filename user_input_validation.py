from user_input_output import user_input_decade, user_input_genre, user_input_movie

# file to include input validation functions


# user_input_validation served to validate the user input which must be an integer between 1 and 6, both inclusive
def user_input_validation(user_input):
    """Given a user inputs, returns True if input is an integer between 1-6 both inclusive, otherwise returns False"""
    if user_input == "":
        raise ValueError("No input provided by user.")
    if not user_input.isdigit():
        raise ValueError("Non digit character detected, only integers allowed.")
    if int(user_input) > 6:
        raise ValueError("User input should be an integer from 1 to 6, maximum value is 6.")
    if int(user_input) < 1:
        raise ValueError("User input should be an integer from 1 to 6, minimum value is 1.")
    return True


# input_validated takes in the user input and checks if the data passes the validation checks, if so it returns True
# otherwise it returns False. This result is then used within user_input_func()
def input_validated(input_raw):
    """Given an input, validates the input and return True if validations passed, otherwise returns False"""
    try:
        user_input_validation(input_raw)

    except ValueError:
        print("Invalid input. Remember that you can only input a number from 1 to 6 for your selection.\n")
        return False

    return True


# user_input_func takes in one of the 3 defined user input function from user_input_output and run it for
# a max of times until a valid input is provided. If the max.tries is exceeded it ends the program
def user_input_func(input_function, tries=0, max_tries=3):
    """Given a function that takes asks and returns user_inputs, allows a max tries to the user and returns input"""
    if tries == max_tries:  # Base case
        print("Sorry, you exceeded the maximum number of tries.")
        return False

    input_raw = input_function()  # Input non validated

    if not input_validated(input_raw) and tries < max_tries:  # If invalid input and tries haven't yet reached max_tries
        tries += 1
        return user_input_func(input_function, tries)  # Recursive function

    return input_raw


# user_input_func(user_input_genre)  # uncomment to test
# user_input_func(user_input_decade)  # uncomment to test
# user_input_func(user_input_movie)  # uncomment to test
