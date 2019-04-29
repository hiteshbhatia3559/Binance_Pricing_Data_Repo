# Todo : Make a library for the program

import numpy
import requests
import datetime
import os

def get_response():
    response = requests.get('https://api.binance.com/api/v1/ticker/allPrices').json()
    return response

def write_coin(pair):
    if os.path.isdir("./data/"+pair['symbol']) is not True:
        os.mkdir("./data/"+pair['symbol'])
    with open("./data/"+pair['symbol']+"/"+str(datetime.datetime.now().date())+".csv","a+") as outfile:
        outfile.write(str(datetime.datetime.now())+","+str(pair['price']+'\n'))
        outfile.flush()
    print("Done for "+str(pair['symbol']+" at "+str(datetime.datetime.now())))


