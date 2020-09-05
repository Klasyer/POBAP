from flask import Flask
from PobapCode.Pricing.PoeNinja import Get_PoeNinja_Item_Price
import json 
from PobapCode.buildNitems.fixedBuild import fixedBuild
from PobapCode.Pricing.Price import Get_Build_Price

app = Flask(__name__) 

@app.route('/Unique/<itemSearch>',methods=['GET'])
def index(itemSearch):
    text = Get_PoeNinja_Item_Price(itemSearch)
    text = json.loads(json.dumps(text))
    return text 

@app.route('/<build>',methods=['GET'])
def finalBuildPricing(build): 
    buildLink = 'https://' + build
    myBuild = fixedBuild(buildLink) 
    myBuild.fix_items()
    rtn = Get_Build_Price(build)
    return rtn


if __name__ == "__main__": 
    app.run(debug=True)