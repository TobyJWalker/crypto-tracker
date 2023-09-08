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

json_data = get_crypto_data()

# display a single data entry provided
def display_single_entry(entry):

    # loop through each item and display
    for (key, value) in entry.items():
        print(f'{key}: {value}')

# displays a list of entries in a clear format
def display_multiple_entries(entries):
    
    # loop through the list of entries
    for entry in entries:

        # display the entry in a clear format and add padding
        display_single_entry(entry)
        print('\n\n')

# get the information of a currency by its symbol as a dictionary
def get_data_by_symbol(symbol, data):

    # loop through data entries
    for entry in data:

        # check if the entry's symbol matches the requested symbol
        if entry['symbol'] == symbol:
            return entry
        
    # return none if no entries we're found
    return None

# get the information of a currency by its symbol as a dictionary
def get_data_by_name(name, data):

    # loop through the data entries
    for entry in data:

        # check to see if the entry's name matches the one specified
        if entry['name'].lower() == name.lower():
            return entry
    
    # return none if no matches are found
    return None

# get currency information by its rank, can't use index as data may not be sorted for rank
def get_data_by_rank(rank, data):

    # loop through data entries
    for entry in data:

        # check to see if ranks match
        if int(entry['rank']) == rank:
            return entry
    

    # return none if rank not found
    return None


display_single_entry(get_data_by_rank(15, json_data))