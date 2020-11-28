import pandas as pd
import pandas_datareader as dr

import bs4
import requests
from bs4 import BeautifulSoup

stocks = {
    "Tesla":"TSLA",
    "Facebook":"FB", 
    "Coke":"COKE", 
    "Apple":"AAPL", 
    "Exxon":"XOM", 
    "American Airlines":"AAL", 
    "Boeing":"BA", 
    "Nike":"NKE", 
    "Six Flags":"SIX", 
    "Amazon":"AMZN", 
    "Chegg":"CHGG", 
    "Cinemark":"CNK", 
    "Lockheed Martin":"LMT",
    "GOOGLE":"GOOGL",
    "McDonalds":"MCD",
    "Walmart":"WMT",
    "Ecana":"OVV",
    "Costco":"COST",
    "Teladoc Health":"TDOC",
    "E*Trade":"ETFC",
    "Beyond Meat":"BYND",
    "iRobot":"IRBT",
    "Alibaba":"BABA",
    "Disney":"DIS",
    "Intel":"INTC",
    "AMD":"AMD",
    "NVIDIA":"NVDA",
    "PepsiCo":"PEP",
    "Fitbit":"FIT",

}

my_stocks = {
    "Tesla":"TSLA",
    "Facebook":"FB",
    "Coke":"COKE", 
    "Apple":"AAPL", 
    "Exxon":"XOM", 
    "American Airlines":"AAL", 
    "Boeing":"BA", 
    "Nike":"NKE", 
    "Lockheed Martin":"LMT",
}

PE_ratios = {}

# was trying to initialize an empty dictionary to use to sort the pe ratios
# [new_dict.setdefault("","") for x in range(4)]


index = 0 
for name, ticker in stocks.items():
    try:
        r = requests.get('https://finance.yahoo.com/quote/' + ticker + '?p=' + ticker + '&.tsrc=fin-srch')
        soup = bs4.BeautifulSoup(r.text,"lxml")

        table = soup.find('table',{'class':'W(100%) M(0) Bdcl(c)'})

        PE_ratio = table.tbody.find("td", {'data-test':"PE_RATIO-value"}).text

        if ticker not in my_stocks.values():
            print(name + ":" + ticker + " - " + PE_ratio)

        if ticker in my_stocks.values():
            print("--- " + name + ":" + ticker + " - " + PE_ratio)

        # PE_ratios[index] = PE_ratio # was going to sort the pe ratios 
        index += 1

    except:
        print(name + " : " + ticker + " - was not found.")

# PE_ratios.sort()
# for r in PE_ratios:
#     print("PE ratio for " + name + " is: " + str(PE_ratio))
