import base64
import re
import requests
import json
import pobapi


def Get_PoePrices_price(item2Price):
    item = {"i":base64.b64encode(item2Price.encode('ascii')) 
    ,"l":"Harvest"
    ,"s":"POBAP"
    }
    poePriceResponse = json.loads((requests.post("https://www.poeprices.info/api?",params=item)).text)
    min_price = poePriceResponse['min']
    max_price = poePriceResponse['max']
    currency = poePriceResponse['currency']
    return {'min':min_price, 'max':max_price, 'currency':currency}

url = "https://pastebin.com/UfSV0JNU" 
#url = "https://pastebin.com/1KTm4QpP"
build = pobapi.from_url(url) 

x = str(build.items[6])

print(Get_PoePrices_price(x))

item = '''Rarity: Rare
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
Hunter Item'''

print(Get_PoePrices_price(item))