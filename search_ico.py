'''
 *************************************************
 * bcStatus - Blockchain Statics Gahter
 * Author: Kanghyo Lee <onyourlife@gmail.com>
 * Copyright (c): 2019, all rights reserved
 * Version: 0.0.1
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 *
 * You may contact the author of bcStatus by e-mail at:
 * onyourlife@gmail.com
 *
 * The latest version of bcStatus can be obtained from:
 * https://github.com/onyourlife/blockchain-information-gather
 *************************************************
'''

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import datetime
import excel
from tqdm import tqdm
from threading import Thread
from bs4 import BeautifulSoup

# get coin list from coingecko
coinList = requests.get("https://api.coingecko.com/api/v3/coins/list").json()

data = []

# Extract Coin ID
for i in tqdm(range(len(coinList))) :    
    coin = requests.get("https://api.coingecko.com/api/v3/coins/"+coinList[i]['id']+"?tickers=true&market_data=true&community_data=true&developer_data=true&sparkline=true").json()
    try:
        if coin['ico_data']['country_origin'] != "KR" :
            data.append(coin['id'] + "|" + coin['name'] + "|" + str(coin['ico_data']['ico_start_date']) + "|" + str(coin['ico_data']['ico_end_date']) + "|" + str(coin['ico_data']['total_raised']) + "|" + str(coin['ico_data']['total_raised_currency']))                       
    except:
        pass

# print(data)

# Save the result on Excel file
excel.makeExcel(data)

print("[*] Finished.")