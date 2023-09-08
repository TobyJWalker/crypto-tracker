import requests
import json

# CoinCap API URL
URL = 'http://api.coincap.io/v2/assets'

''' Example layout
{
      "id": "bitcoin",
      "rank": "1",
      "symbol": "BTC",
      "name": "Bitcoin",
      "supply": "17193925.0000000000000000",
      "maxSupply": "21000000.0000000000000000",
      "marketCapUsd": "119150835874.4699281625807300",
      "volumeUsd24Hr": "2927959461.1750323310959460",
      "priceUsd": "6929.8217756835584756",
      "changePercent24Hr": "-0.8101417214350335",
      "vwap24Hr": "7175.0663247679233209"
    }
'''

# get the current crypto data from CoinCap API
def get_crypto_data():
    
    # make a GET request to retrieve all current cryptocurrency data
    response = requests.get(URL)
    
    # parse the data into json format and return the data portion
    parsed_data = json.loads(response.text)
    return parsed_data['data']

# get the information of a currency by its symbol as a dictionary
def get_data_by_symbol(symbol, data):

    # loop through data and return the data entry which matches the requested symbol
    for entry in data:
        if entry['symbol'] == 'symbol':
            return entry
    return None