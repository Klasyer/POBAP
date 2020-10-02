from flask import Flask, request
from PobapCode.Pricing.PoeNinja import Get_PoeNinja_Item_Price
import json 
from PobapCode.buildNitems.fixedBuild import fixedBuild
from PobapCode.Pricing.Price import Get_Build_Price

application = app = Flask(__name__) 

#since poe.ninja only provides full lists of items and prices, and i had to make a way to get only 1 item price, i made this to pull 1 uniques price 
@application.route('/Unique/<itemSearch>',methods=['GET'])
def UniuqePrice(itemSearch):
    text = Get_PoeNinja_Item_Price(itemSearch)
    text = json.loads(json.dumps(text))
    return text 

#takes a build pastebin, and returns a json file with the estimated prices for each item and the total cost of the build 
@application.route('/pastebin.com/<build>',methods=['GET'])
def finalBuildPricing_Pastebin(build): 
    buildLink = 'https://pastebin.com/' + build
    myBuild = fixedBuild(buildLink) 
    myBuild.fix_items()
    rtn = json.loads(json.dumps(Get_Build_Price(myBuild)))
    return rtn

#takes a build XNL, and returns a json file with the estimated prices for each item and the total cost of the build 
@application.route('/PriceXml',methods=['POST'])
def finalBuildPricing_XML(): 
    buildLink = request.data
    myBuild = fixedBuild(buildLink) 
    myBuild.fix_items()
    rtn = json.loads(json.dumps(Get_Build_Price(myBuild)))
    return rtn

if __name__ == "__main__": 
    app.run(debug=False)