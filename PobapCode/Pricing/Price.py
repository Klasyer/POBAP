from PobapCode.buildNitems.fixedBuild import fixedBuild
from PobapCode.buildNitems.fixedItem import fixedItem
from PobapCode.Pricing.PoePrices import Get_PoePrices_price
from PobapCode.Pricing.PoeNinja import Get_PoeNinja_Item_Price, Get_Chaos, Get_From_Chaos
from PobapCode.Pricing.cache import BuildCache
from cachetools import cached

@cached(BuildCache)
def Get_Build_Price(fixedBuild): 
    pricedBuild = []
    totPrice = 0 
    uniqueCount = 0
    for i,item in enumerate(fixedBuild.buildItems): 
        if fixedBuild.originalBuild.items[i].rarity == 'Unique': 
            fxitem = fixedItem(fixedBuild.buildItems[i])
            price = Get_PoeNinja_Item_Price(fixedBuild.originalBuild.items[i].name,fxitem.item_links())
            uniqueCount = uniqueCount + 1 
        else:
            price = Get_PoePrices_price(('\n'.join(map(str,item))),fixedBuild.originalBuild.items[i].name)
        if price['currency'] != 'chaos':
            totPrice = totPrice + Get_Chaos(price['value'],price['currency'])
        else: 
            totPrice = totPrice + price['value']
        pricedBuild.append(price)
    totPrice = round(totPrice,2)
    totExalted = round(Get_From_Chaos(totPrice,'exalted'),2)
    total = {'Chaos Total Cost':totPrice,'Currency':'chaos','Exalted Total Cost':totExalted, 'Unique Items':uniqueCount} 
    finalPricing = {'Overview':total, 'Detialed':pricedBuild}
    return finalPricing 
0
'''
b1 = fixedBuild("https://pastebin.com/UfSV0JNU")

b1.fix_items()

print(Get_Build_Price(b1)) 
'''