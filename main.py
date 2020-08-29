from PoeNinja import Get_PoeNinja_Prices
import time 
from flask import Flask
import json 

app = Flask(__name__) 

@app.route('/')
def index(): 
    return json.loads('This Worked')

if __name__ == "__main__": 
    app.run(debug=True)

    