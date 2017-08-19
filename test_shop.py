import requests
import sys, os
import random
import json
import re

def asics(max_price=100):
    URL = 'http://www.onitsukatiger.com/us/en-us/mens/c/mens-shoes?q=:relevance:gender:MALE:shoeSizeCode:10.5:model:Colorado%20Eighty-Five'

    def html_source(URL):
        return requests.get(URL).text

    def make_regex():
        ips = ['initArr.ecommerce =  (.*)']
        products = "".join(ips)
        return products

    def make_regex2():
        ips = ['<p class="price center">\n\t\$(.*?)</p>']
        prices = "".join(ips)
        return prices

    def get_sales(products, max_price):
        print(products)
        return [i for i in products if float(i['price']) < max_price ]

    def rejection():
        rejects = ['nah.', 'nope.', 'nope', 'nada', 'nothing', 'nil', 'no.', 'not today', 'sorry about it', 'not yet', 'patience is a virtue']
        return random.choice(rejects)


    myObject = re.findall(make_regex(), html_source(URL))
    shoes = json.loads(myObject[0][:-2])
    shoes_list = shoes['impressions']


    quant = len(get_sales(products=shoes_list, max_price=max_price))

    if quant >0:
        text = 'hey john luck there are {} shoes that would interest you!'.format(quant)
    else:
        text = rejection()
    return {'Text': text, 'Max_Price': max_price}

def jcrew(max_price=50):
    URL = 'https://www.jcrew.com/search2/index.jsp?N=21+16+10002+11998&Nloc=en&Ntrm=&Npge=1&Nrpp=48&Nsrt=3&hasSplitResults=false'

    def html_source(URL):
        return requests.get(URL).text

    def make_regex():
        ips = ['pageJson: (.*),']
        products = "".join(ips)
        return products

    def make_regex2():
        ips = ['navigationInfo : (.*),']
        prices = "".join(ips)
        return prices

    def make_regex3():
        ips = ['i>In stores & online:</i> (.*?)%', 'off']
        prices = "".join(ips)
        print(ips)
        return prices

    def get_sales(products, max_price, discount):
        return [i for i in products if float(i['salePrice']) * (1-discount) < max_price*100 ]

    def rejection():
        rejects = ['nah.', 'nope.', 'nope', 'nada', 'nothing', 'nil', 'no.', 'not today', 'sorry about it', 'not yet', 'patience is a virtue']
        return random.choice(rejects)

    def get_discount():
        try:
            discount = re.findall(make_regex2(), html_source(URL))
            myJson =  json.loads(discount[0])
            final_discount = myJson['data']['nav'][1]['navGroups'][0]['navItems'][1]['label']
            return re.sub(r'[^0-9]', '', str(final_discount)) #numbers only
        except:
            try:
                discount = re.findall(make_regex3(), html_source(URL))[0]
                return re.sub(r'[^0-9]', '', str(discount)) #numbers only
            except:
                return 1

    myObject = re.findall(make_regex(), html_source(URL))
    shirts = json.loads(myObject[0])
    shirts_list = shirts['search']['results']['products']
    discount= float(str(get_discount())[0:2])/100


    print('the discount is {}%'.format(discount)) #error handling


    quant = len(get_sales(products=shirts_list, max_price=max_price, discount=discount))

    if quant >0:
        text = 'yoooo juan lucas there are {} shirts that may fit you, since the discount is {}%'.format(quant, int(discount*100))
    else:
        text = rejection()

    return {'Text': text, 'Max_Price': max_price}


if __name__ == "__main__":
    print(jcrew())
