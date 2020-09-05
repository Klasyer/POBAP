import requests 
import json 
import time 
import os 
from PobapCode.Pricing.cache import PoeNinjaCache,PriceCache, CurrencyCache
from cachetools import cached
from PobapCode.needed.neededLists import poeNinja_links, poeNinja_Currency
import pickle 

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

@cached(PriceCache)
def Get_PoeNinja_Item_Price(item2Price,links = 0): 
    price = 0
    for item in Get_PoeNinja_Prices(): 
        if item['name'] == item2Price and item['links'] == links: 
            price = item['value']
    rtn = {'name':item2Price, 'value':price, 'currency':'chaos'}
    return rtn

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

'''
for item in Get_PoeNinja_Currency():
    #print(item)
    return 1
'''
