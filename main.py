import requests
import time

from config import API_TOKEN, WALLET_ADRESS



params = {"module": "account", "action": "txlist","address": WALLET_ADRESS,
          "startblock": 0, "endblock": 99999999, "page": 1, "offset": 10,
          "sort": "desc", "apikey": API_TOKEN}

r = requests.get("https://api.bscscan.com/api", params=params)
txlist_result = r.json()["result"]

#check the existence of transactions
if r.json()["message"] == "No transactions found":
    raise Exception("No transactions found")

count_txlist = len(txlist_result)
timeslamp_txlist = [int(d["timeStamp"]) for d in txlist_result]



while True:
    r = requests.get("https://api.bscscan.com/api", params=params)
    txlist_result = r.json()["result"]

    for tx in txlist_result:
        if int(tx["timeStamp"]) not in timeslamp_txlist:
            print("Новая транзакция:", tx["hash"])
    timeslamp_txlist = [int(d["timeStamp"]) for d in txlist_result]
    time.sleep(1)
