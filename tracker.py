import requests
import json

# CoinCap API URL
URL = 'http://api.coincap.io/v2/assets'

# get the current crypto data from CoinCap API
def get_crypto_data():
    
    # make a GET request to retrieve all current cryptocurrency data
    response = requests.get(URL)
    
    # parse the data into json format and return the data portion
    parsed_data = json.loads(response.text)
    return parsed_data['data']

