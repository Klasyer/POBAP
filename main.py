import time 
from flask import Flask
from PobapCode.Pricing.PoeNinja import Get_PoeNinja_Item_Price
import json 

app = Flask(__name__) 

@app.route('/Unique/<itemSearch>',methods=['GET'])
def index(itemSearch):
    text = Get_PoeNinja_Item_Price(itemSearch)
    text = json.loads(json.dumps(text))
    return text 



if __name__ == "__main__": 
    app.run(debug=True)
