from flask import Flask
import requests
from bs4 import BeautifulSoup
from createProductsList import createProductsList
import json
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    print('in api /')
    return "<p style={background-color: black;}>Hello, World!</p>"
#34
@app.route("/parseShop")
def parseShop():
    products = []
    cat = "CARNE"
    subCat = "Promozioni"
    url = 'https://www.carrefour.it/spesa-online/carne/#size=75&position=3960'
    resp = requests.get(url)
    html = resp.content
    soup = BeautifulSoup(html, 'html.parser' )
    products1 = createProductsList(soup, cat, subCat)
    # further commented need when products list contains of many pages
    # for i in range(1, 2):
    #     print(i)
    #     resp = requests.get(url+str(i))
    #     html = resp.content
    #     soup = BeautifulSoup(html, 'html.parser' )
    #     products.extend(createProductsList(soup, cat, subCat))
        
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "shops.json")
    openedFile = open(json_url,'w')
    # print(products1)
    openedFile.writelines(products1)#[1:][:-1])+', ')
    openedFile.close()
    return {}
    # return products1

app.run(host="0.0.0.0", port=5000, debug=True)