# FILE INFO: contains functions and variable utils used in the other files across the project.


def decorator_underscore(func):
    def inner_wrapper(*args, **kwargs):
        print("_" * 30)
        func(*args, **kwargs)
        print("_" * 30)
    return inner_wrapper


def decorator_empty_line(func):
    def inner_wrapper(*args, **kwargs):
        print("\n")
        func(*args, **kwargs)
        print("\n")
    return inner_wrapper


def decorator_stars(func):
    def inner_wrapper(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner_wrapper


# The below aims to capture the names of the providers we will be showing in our front end only (6 providers only to
# include: Nextflix, BBC, Sky, Amazon, Apple and Disney"
def provider_names_to_user(providers_movie):
    """Given a list of streaming providers, returns a set of providers within the selection made"""
    providers_user = set()
    for provider in providers_movie:
        if provider.startswith("Amazon"):
            providers_user.add("Amazon")
        elif provider.startswith("Apple"):
            providers_user.add("Apple")
        elif provider.startswith("BBC"):
            providers_user.add("BBC")
        elif provider.startswith("Disney"):
            providers_user.add("Disney")
        elif provider.startswith("Netflix"):
            providers_user.add("Netflix")
        elif provider.startswith("Sky"):
            providers_user.add("Sky")
        else:
            continue
    if len(providers_user) == 0:
        return "No UK streaming availability for Amazon, Apple, BBC, Disney, Netflix or Sky"
    return providers_user


# Dictionary containing as keys the streaming providers and as value the URL to access
providers_url = {"Amazon": "https://www.amazon.co.uk/Amazon-Video/b?node=3010085031",
                 "Apple": "https://www.apple.com/uk/apple-tv-plus/",
                 "BBC": "https://www.bbc.co.uk/iplayer/live/bbcone",
                 "Disney": "https://www.disneyplus.com/en-ch",
                 "Netflix": "https://www.netflix.com/ch-en/",
                 "Sky": "https://www.sky.com/watch"}


# providers list contains all the UK streaming providers analysed by TheMovieDM API as of May 2022.
# The information has been retrieved using the function _streaming_providers_uk from api_requests_streaming
providers = ['ARROW', 'Acorn TV', 'AcornTV Amazon Channel', 'All 4', 'Amazon Prime Video', 'Amazon Video',
             'Apple TV Plus', 'Apple iTunes', 'Argo', 'Arrow Video Amazon Channel', 'BBC iPlayer', 'BFI Player',
             'BFI Player Amazon Channel', 'BritBox', 'BritBox Amazon Channel', 'BroadwayHD', 'Chili', 'Classix',
             'Cultpix', 'Curiosity Stream', 'CuriosityStream Amazon Channel', 'Curzon Home Cinema', 'DOCSVILLE',
             'Dekkoo', 'Discovery Plus', 'Discovery+ Amazon Channel', 'Disney Plus', 'DocAlliance Films',
             'DocuBay Amazon Channel', 'Dogwoof On Demand', 'Eros Now Amazon Channel', 'Eventive',
             'Fandor Amazon Channel', 'FilmBox Live Amazon Channel', 'FilmBox+', 'Filmzie', 'Flix Premiere',
             'Freevee Amazon Channel', 'Full Moon Amazon Channel', 'Funimation Now', 'Google Play Movies', 'GuideDoc',
             'HiDive', 'Hoichoi', 'ITV Hub', 'MGM Amazon Channel', 'Magellan TV', 'Microsoft Store',
             'MotorTrend Amazon Channel', 'Mubi', 'Mubi Amazon Channel', 'My5', 'Netflix', 'Netflix Kids', 'Now TV',
             'Now TV Cinema', 'Pantaflix', 'Paus', 'Plex', 'Pluto TV', 'Pokémon Amazon Channel', 'Rakuten TV', 'Revry',
             'STUDIOCANAL PRESENTS Apple TV Channel', 'STV Player', 'ShortsTV Amazon Channel',
             'Shout! Factory Amazon Channel', 'Shudder', 'Shudder Amazon Channel', 'Sky Go', 'Sky Store', 'Spamflix',
             'Starz', 'Starz Play Amazon Channel', 'True Story', 'Virgin TV Go', 'W4free', 'WOW Presents Plus',
             'YouTube', 'YouTube Premium']
