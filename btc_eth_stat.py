#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import datetime
from bs4 import BeautifulSoup

def callAPI(url, field):
    r = requests.get(url).json()
    return str(format(r[field],','))

def getDBSize(platform):
    url = 'https://bitinfocharts.com/' + platform + '/'
    r = requests.get(url)
    c = r.text

    soup = BeautifulSoup(c, 'html.parser')
    itemList = soup.findAll('td',{'id':'tdid23'})
    for data in itemList:
        print(str(platform).capitalize() + " DB Size : " + str(data.get_text()))

def getEthNodes():
    url = 'https://etherscan.io/nodetracker/'
    r = requests.get(url)
    c = r.text

    soup = BeautifulSoup(c, 'html.parser')
    itemList = soup.findAll('strong',{'class':'text-dark'})
    for data in itemList:
        print("Ethereum Nodes : " + str(data.get_text()))

def getEthTx():
    url = 'https://etherscan.io/txs'
    r = requests.get(url)
    c = r.text

    soup = BeautifulSoup(c, 'html.parser')
    itemList = soup.findAll('span',{'class':'d-flex align-items-center'})
    for data in itemList:
        print("Ethereum Tx : " + data.get_text()[14:][:-18])


if __name__ == "__main__":
        print(datetime.datetime.now())
        ### Bitcoin
        #userCoordinateUrl = 'https://bitnodes.earn.com/api/v1/snapshots/latest/?field=coordinates'
        userAgentNodeUrl = 'https://bitnodes.earn.com/api/v1/snapshots/latest/?field=user_agents'
        btcStatsUrl = 'https://api.blockchain.info/stats'

        ### The Number of Bitcoin Nodes
        print("======= Bitcoin =======")
        #print("Bitcoin Nodes(coordinates) : " + callAPI(userCoordinateUrl, 'total_nodes'))
        print("Bitcoin Nodes : " + callAPI(userAgentNodeUrl, 'total_nodes'))
        print("Bitcoin Tx : " + callAPI(btcStatsUrl, 'n_tx'))
        getDBSize("bitcoin")
        print("\n")
        print("======= Ethereum =======")
        getEthNodes()
        getEthTx()
        getDBSize("ethereum")