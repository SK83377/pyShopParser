import re

def createProductsList(listHtml, cat, subCat):
    productsPerPage = []
    for li in listHtml.find_all('div', attrs={'class':'product-item'}):
        # print(li)
        prodItem = {}
        prodItem["ean"] = ""
        prodItem["categories"] = [
            {
                "url": "",
                "name": cat
            },
            {
                "url": "",
                "name": subCat
            }
        ]
        prodItem["url"] = ""
        prodItem["name"] = li.find('h3', attrs={'class':'tile-description'}).getText()
        prodItem["brand"] = li.find('h2', attrs={'class':'brand'}).getText()
        prodItem["price"] = li.find('span', attrs={'class':'value'})['content']#.getText()[1:][:-3]
        prodItem["image"] = ''
        productsPerPage.append(prodItem)
        # print(prodItem)
        
    return productsPerPage

    exmpl = [
        {
            "ean": "8017619720115",
            "categories": [
            {
                "url": "",
                "name": "ALIMENTARI"
            },
            {
                "url": "",
                "name": "CIBI INFANZIA"
            }
            ],
            "url": "",
            "name": "Aptamil 3 Latte Crescita Lt.1",
            "brand": "Aptamil",
            "price": "2.19",
            "image": ""
        }
    ]
