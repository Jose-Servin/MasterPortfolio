"""
DESCRIPTION: Scrape Honda Accord information
AUTH: Jose Servin

"""
import pandas as pd


BASE_URL = 'https://www.carmax.com/'
SIGN_IN_URL = BASE_URL + "/mycarmax/sign-in"


# Sign into CarMax using test account
