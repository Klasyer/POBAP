from flask import Flask, request
from PobapCode.Pricing.PoeNinja import Get_PoeNinja_Item_Price
import json 
from PobapCode.buildNitems.fixedBuild import fixedBuild
from PobapCode.Pricing.Price import Get_Build_Price

application = app = Flask(__name__) 

@app.route('/Unique/<itemSearch>',methods=['GET'])
def UniuqePrice(itemSearch):
    text = Get_PoeNinja_Item_Price(itemSearch)
    text = json.loads(json.dumps(text))
    return text 

@app.route('/pastebin.com/<build>',methods=['GET'])
def finalBuildPricing_Pastebin(build): 
    buildLink = 'https://pastebin.com/' + build
    myBuild = fixedBuild(buildLink) 
    myBuild.fix_items()
    rtn = json.loads(json.dumps(Get_Build_Price(myBuild)))
    return rtn

@app.route('/PriceXml',methods=['POST'])
def finalBuildPricing_XML(): 
    buildLink = request.data
    myBuild = fixedBuild(buildLink) 
    myBuild.fix_items()
    rtn = json.loads(json.dumps(Get_Build_Price(myBuild)))
    return rtn

if __name__ == "__main__": 
    app.run(debug=False)