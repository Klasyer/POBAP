import requests 
import json 
import time 
import os 
from cache import PoeNinjaCache, PriceCache
from cachetools import cached
from needed.neededLists import poeNinja_links 
import pickle 

@cached(PoeNinjaCache)
def Get_PoeNinja_Prices(): 
    toUpdate = False 
    timeNow = time.time() 
    if os.stat("Pricing\PoeNinjaPrices.txt").st_size == 0: 
        toUpdate = True
    else: 
        with open ('Pricing\PoeNinjaPrices.txt', 'rb') as fp:
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
        with open('Pricing\PoeNinjaPrices.txt', 'wb') as fp:
            pickle.dump(PoeNinjaPrice, fp)
    return PoeNinjaPrice 

@cached(PriceCache)
def Get_PoeNinja_Item_Price(item2Price): 
    price = '???'
    for item in Get_PoeNinja_Prices(): 
        if item['name'] == item2Price: 
            price = item['value']
    rtn = {'name':item2Price, 'value':price, 'currency':'chaos'}
    return rtn

