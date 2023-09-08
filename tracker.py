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

    # validate the data type of symbol and handle accordingly
    if type(symbol) == str:

        # loop through data entries
        for entry in data:

            # check to see if symbols match
            if entry['symbol'].lower() == symbol.lower():
                return entry
        
        # return None if symbol not found
        return None
            
    elif type(symbol) == list:

        # turn all symbols lowercase for case-insensitivity
        symbol = [c.lower() for c in symbol]

        
        # create a list of entries
        entries = []

        # loop through data entries
        for entry in data:

            # check to see if entry's symbol is requested 
            if entry['symbol'].lower() in symbol:

                # add to list of entries
                entries.append(entry)
        
        return entries if entries != [] else None
    
    else:
        # return none if symbol is incorrect data type
        return None

# get the information of a currency by its name
def get_data_by_name(name, data):

    # validate the data type of name and handle accordingly
    if type(name) == str:

        # loop through data entries
        for entry in data:

            # check to see if names match
            if entry['name'] == name:
                return entry
        
        # return None if name not found
        return None
            
    elif type(name) == list:

        # turn all names lowercase for case-insensitivity
        name = [c.lower() for c in name]

        
        # create a list of entries
        entries = []

        # loop through data entries
        for entry in data:

            # check to see if entry's name is requested 
            if entry['name'].lower() in name:

                # add to list of entries
                entries.append(entry)
        
        return entries if entries != [] else None
    
    else:
        # return none if rank is incorrect data type
        return None

# get currency information by its rank, can't use index as data may not be sorted for rank
def get_data_by_rank(rank, data):

    # validate the data type of rank and handle accordingly
    if type(rank) == int:

        # loop through data entries
        for entry in data:

            # check to see if ranks match
            if int(entry['rank']) == rank:
                return entry
        
        # return None if rank not found
        return None
            
    elif type(rank) == list:
        
        # create a list of entries
        entries = []

        # loop through data entries
        for entry in data:

            # check to see if entry's rank is requested 
            if int(entry['rank']) in rank:

                # add to list of entries
                entries.append(entry)
        
        return entries if entries != [] else None
    
    else:
        # return none if rank is incorrect data type
        return None

# sorting function which takes the value to sort by as a parameter
def sort_by(value, data, reverse=False):

    # categorise the possible values into lists or strings
    str_vals = ['id', 'symbol', 'name', 'explorer']
    num_vals = ['rank', 'supply', 'marketCapUsd', 'volumeUsd24Hr', 'priceUsd', 'changePercent24Hr', 'vwap24Hr']

    # try to sort by the provided value, catch error if value doesn't exist
    if value in str_vals:
        return list(sorted(data, key=lambda entry: entry[value], reverse=reverse))
    elif value in num_vals:
        return list(sorted(data, key=lambda entry: float(entry[value]), reverse=reverse))
    elif value == 'maxSupply':
        return list(sorted(data, key=lambda entry: float(entry[value]) if entry[value] != None else 10**20, reverse=reverse))  
    else:
        print('''Invalid value type. Options are:
              id
              rank
              symbol
              name
              supply
              marketCapUsd
              volumeUsd24Hr
              priceUsd
              changePercent24Hr
              vwap24Hr
              explorer
              ''')
        return None

if __name__ == '__main__':
    display_multiple_entries(sort_by('maxSupply', json_data, reverse=False)[:5])