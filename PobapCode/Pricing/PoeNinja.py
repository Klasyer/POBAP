import requests 
import json 
import time 
import os 
from PobapCode.Pricing.cache import PoeNinjaCache,PriceCache, CurrencyCache, ChaosCache, FromChaosCache
from cachetools import cached
from PobapCode.needed.neededLists import poeNinja_links, poeNinja_Currency
import pickle 
import re

#we are updating once every 24 hours the list with the prices for all the items from poeNinja
@cached(PoeNinjaCache)
def Get_PoeNinja_Prices(): 
    toUpdate = False 
    timeNow = time.time() 
    if os.stat("PobapCode\Pricing\PoeNinjaPrices.txt").st_size == 0: 
        toUpdate = True
    else: 
        with open ('PobapCode\Pricing\PoeNinjaPrices.txt', 'rb') as fp:
            PoeNinjaPrice = pickle.load(fp)
        if timeNow - PoeNinjaPrice[0]['value'] > 43200: 
            toUpdate = True 

    if toUpdate: 
        fileTime = dict(name='ListTime',links='0',value=time.time())
        PoeNinjaPrice = [fileTime]
        linksList = poeNinja_links 
        for link in linksList: 
            r = requests.get(link) 
            priceList = json.loads(r.text) 
            for item in priceList['lines']: 
                itemProps = dict(name=item['name'],links=item['links'],value=item['chaosValue'])
                PoeNinjaPrice.append(itemProps)
        with open('PobapCode\Pricing\PoeNinjaPrices.txt', 'wb') as fp:
            pickle.dump(PoeNinjaPrice, fp)
    return PoeNinjaPrice 

#For an item requested, we are returning the item, and its value (chaos value atm, other option soonTM to come) 
@cached(PriceCache)
def Get_PoeNinja_Item_Price(item2Price,links = 0): 
    price = 0
    fnlPrice = 0 
    for item in Get_PoeNinja_Prices(): 
        if item['name'] == item2Price and item['links'] == links: 
            price = item['value']
    fnlPrice = max(fnlPrice,price)
    rtn = {'name':item2Price, 'value':fnlPrice, 'currency':'chaos'}
    return rtn

#simmilarly to before, here we get the full list once every 24 hours of all the currency values
@cached(CurrencyCache)
def Get_PoeNinja_Currency(): 
    toUpdate = False 
    timeNow = time.time() 
    if os.stat("PobapCode\Pricing\PoeNinjaCurrency.txt").st_size == 0: 
        toUpdate = True
    else: 
        with open ('PobapCode\Pricing\PoeNinjaCurrency.txt', 'rb') as fp:
            PoeNinjaCurrency = pickle.load(fp)
        if timeNow - PoeNinjaCurrency[0]['value'] > 43200: 
            toUpdate = True 

    if toUpdate: 
        fileTime = dict(name='ListTime',value=time.time())
        PoeNinjaCurrency = [fileTime]
        linksList = poeNinja_Currency 
        for link in linksList: 
            r = requests.get(link) 
            priceList = json.loads(r.text) 
            for item in priceList['lines']: 
                itemProps = dict(name=item['currencyTypeName'],value=item['receive']['value'])
                PoeNinjaCurrency.append(itemProps)
        with open('PobapCode\Pricing\PoeNinjaCurrency.txt', 'wb') as fp:
            pickle.dump(PoeNinjaCurrency, fp)
    return PoeNinjaCurrency 

#gets the chaos value of a currency 
@cached(ChaosCache)
def Get_Chaos(amount, currency): 
    price = 0 
    for item in Get_PoeNinja_Currency():
        name = item['name'].upper()
        name = re.sub(' ORB$','',name)
        if currency.upper() == name:
            price = amount * item['value']
    if price == 0: 
        price = amount
    return price

#translates chaos value to a different currency
@cached(FromChaosCache)
def Get_From_Chaos(chaosAmount, currency): 
    price = 0 
    for item in Get_PoeNinja_Currency():
        name = item['name'].upper()
        name = re.sub(' ORB$','',name)
        if currency.upper() == name:
            price = chaosAmount / item['value']
    if price == 0: 
        price = chaosAmount
    return price