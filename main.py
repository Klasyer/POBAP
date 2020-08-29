from PoeNinja import Get_PoeNinja_Prices
import time 
from flask import Flask
import json 

app = Flask(__name__) 

@app.route('/<itemSearch>',methods=['GET'])
def index(itemSearch):
    price = "???"
    for item in Get_PoeNinja_Prices(): 
        if item['name'] == itemSearch: 
            price = item['valaue']
    text =  "%s costs %s" %  (itemSearch,price)
    text = json.loads(json.dumps(text))
    return text 

if __name__ == "__main__": 
    app.run(debug=True)

    