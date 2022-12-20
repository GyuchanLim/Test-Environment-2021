import json
import os

filename = os.getcwd() + '/CSV/market-price-2.json'

f = open(filename)
data = json.load(f)

print()