import datetime
import requests
from lib import *
from time import sleep

# print()

if __name__ == '__main__':
    # print()
    while True:
        data = get_response()
        for coin in data:
            write_coin(coin)
        sleep(1)
