import requests
import time
import json
import hmac
import hashlib

timestamp = int(time.time()*1000)
query_string = 'timestamp={}'.format(timestamp)
secret = 'SECRET API'
signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
#print(signature)

url = "https://testnet.binance.vision/api/v3/account?timestamp={}&signature={}".format(timestamp, signature)
#print(url)

payload={}
headers = {
  'Content-Type': 'application/json',
  'X-MBX-APIKEY': 'YOUR API'
}

response = (requests.request("GET", url, headers=headers, data=payload)).json()

#print(response)
balance = response['balances']
for i in balance:
  if i['asset']=='BTC':
    print(i['free'])