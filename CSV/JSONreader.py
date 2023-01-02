import json
import os
import datetime

def print_array(list):
    for x in list:
        print(x, end='|type is ')
        print(type(x))

def load_data():
    filename = os.getcwd() + '/CSV/market-price-2.json'

    f = open(filename)
    data = json.load(f)
    
    return data

def UTC_milisecond_to_datetime(time_price_dictionary):
    for dictionary in time_price_dictionary:
        print(datetime.datetime.fromtimestamp(dictionary['x']/1000.0), end = '')
        print(dictionary['y'])

data = load_data()

UTC_milisecond_to_datetime(data['market-price'])

"""
market_price = data['market-price']

print_array(market_price)
print(datetime.datetime.fromtimestamp(1671321600000/1000.0))
"""