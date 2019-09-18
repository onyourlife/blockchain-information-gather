#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import datetime
from bs4 import BeautifulSoup

coinList = requests.get("https://api.coingecko.com/api/v3/coins/list").json()

fw = open('ICO.txt','w')

# Extract Coin ID
for i in range(len(coinList)) :    
    coin = requests.get("https://api.coingecko.com/api/v3/coins/"+coinList[i]['id']+"?tickers=true&market_data=true&community_data=true&developer_data=true&sparkline=true").json()
    try:
        if coin['ico_data']['country_origin'] != "KR" :
            fw.write("ID : " + coin['id'] + ", NAME : " + coin['name'] + ", ICO 시작일 : " + str(coin['ico_data']['ico_start_date']) + ", ICO 종료일 : " + str(coin['ico_data']['ico_end_date']) + ", ICO 총 상장액 : " + str(coin['ico_data']['total_raised']) + " " + str(coin['ico_data']['total_raised_currency'])+"\n")                    
            print("ID : " + coin['id'])
            #print("ID : " + coin['id'] + ", NAME : " + coin['name'] + ", ICO 시작일 : " + str(coin['ico_data']['ico_start_date']) + ", ICO 종료일 : " + str(coin['ico_data']['ico_end_date']) + ", ICO 총 상장액 : " + str(coin['ico_data']['total_raised']) + " " + str(coin['ico_data']['total_raised_currency']))
            '''
            print("ID : " + coin['id'] + ", " + "NAME : " + coin['name'])
            print("ICO 시작일 : " + str(coin['ico_data']['ico_start_date']))
            print("ICO 종료일 : " + str(coin['ico_data']['ico_end_date']))
            print("ICO 총 상장액 : " + str(coin['ico_data']['total_raised'] + " " + str(coin['ico_data']['total_raised_currency'])))
            '''
    except:
        pass

fw.close()
print("[*] Finished.")
