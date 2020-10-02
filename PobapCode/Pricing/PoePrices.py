import base64
import re
import requests
import json
import pobapi
from PobapCode.Pricing.cache import PoePriceCache
from cachetools import cached

#for league l, we are sending an item (after its fixed) to poePrices, jsoning the responce and getting out the maximum price of the item. 
#because poeNinja and poePrices write ex in different ways we replace it
#then we return the price back, with the item

@cached(PoePriceCache)
def Get_PoePrices_price(item2Price,itemName):
    item = {"i":base64.b64encode(item2Price.encode('ascii')) 
    ,"l":"Heist"
    ,"s":"POBAP"
    }
    poePriceResponse = json.loads((requests.post("https://www.poeprices.info/api?",params=item)).text)
    try: 
        max_price = round(poePriceResponse['max'],2)
        currency = poePriceResponse['currency'].replace('exalt','exalted')
    except: 
        max_price = 0 
        currency = 'chaos'
    return {'name':itemName,'value':max_price, 'currency':currency}


'''
url = "https://pastebin.com/UfSV0JNU" 
#url = "https://pastebin.com/1KTm4QpP"
build = pobapi.from_url(url) 

x = str(build.items[6])
y = build.items[6].name

print(x)

print(Get_PoePrices_price(x,y))

item = Rarity: Rare
Oblivion Veil
Astral Plate
--------
Quality: +28% (augmented)
Armour: 711
--------
Requirements:
Level: 72
Str: 180
Dex: 111
Int: 155
--------
Sockets: G-B-W-G-B-G 
--------

Item Level: 86
--------
Quality does not increase Defences (enchant)
Grants +1 to Maximum Life per 2% Quality (enchant)
--------
+12% to all Elemental Resistances (implicit)
--------
11% increased Intelligence
+119 to maximum Life
You can apply an additional Curse
Enemies you Kill Explode, dealing 3% of their Life as Physical Damage
Spells have +1.48% to Critical Strike Chance 
+15% to Fire and Chaos Resistances (crafted)
--------
Crusader Item
Hunter Item
'''

#print(Get_PoePrices_price(item,'Oblivion Veil'))
