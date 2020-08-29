import requests 
import json 
import datetime 
from cache import cache
from cachetools import cached

@cached(cache)
def Get_PoeNinja_Prices(): 
    PoeNinjaPrice = [] 
    links = open('PoeNinjaLinks.txt', 'r') 
    linksList = links.read().splitlines()
    for link in linksList: 
        r = requests.get(link) 
        priceList = json.loads(r.text) 
        for item in priceList['lines']: 
            itemProps = [] 
            itemProps.append(item['name'])
            itemProps.append(item['links'])
            itemProps.append(item['chaosValue'])
            PoeNinjaPrice.append(itemProps)
    return PoeNinjaPrice 





