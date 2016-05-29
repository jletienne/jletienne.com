import requests
import sys, os
import random
import json
import re

def asics():
    URL = 'http://www.onitsukatiger.com/us/en-us/mens/c/mens-shoes?q=:relevance:gender:MALE:shoeSizeCode:10.5:model:Colorado%20Eighty-Five'
    def html_source(URL):
        return requests.get(URL).text

    def make_regex():
        ips = ['<div class="fullProdName">(.*?)</div>']
        products = "".join(ips)
        return products

    def make_regex2():
        ips = ['<p class="price center">\n\t\$(.*?)</p>']
        prices = "".join(ips)
        return prices

    def get_sales(products, max_price):
        return [i for i in products if i[0] < max_price ]

    def rejection():
        rejects = ['nah.', 'nope.', 'nope', 'nada', 'nothing', 'nil', 'no.', 'not today', 'sorry about it', 'not yet', 'patience is a virtue']
        return random.choice(rejects)

    shoes = re.findall(make_regex(), html_source(URL))
    costs = [float(i) for i in re.findall(make_regex2(), html_source(URL))]
    products = list(zip(costs,shoes))

    quant = len(get_sales(products=products, max_price = 100))

    if quant >0:
        return('hey john luck there are {} shoes that would interest you'.format(quant))
    else:
        return(rejection())

def jcrew():
    URL = 'https://www.jcrew.com/search2/index.jsp?N=21+16+10002+11998&Nloc=en&Ntrm=&Npge=1&Nrpp=48&Nsrt=3&hasSplitResults=false'

    def html_source(URL):
        #print(requests.get(URL).text)
        return requests.get(URL).text

    def make_regex():
        ips = ['now <span class="product-sale-price notranslate">\s*\$(.*)</span>']
        products = "".join(ips)
        return products

    def make_regex2():
        ips = ['<a href="https://www.jcrew.com/sale.jsp">extra (.*?)%']
        prices = "".join(ips)
        return prices

    def make_regex3():
        ips = ['i>In stores & online:</i> (.*?)%', ' off']
        prices = "".join(ips)
        return prices

    def get_sales(products, max_price):
        return [i for i in products if i < max_price ]

    def rejection():
        rejects = ['nah.', 'nope.', 'nope', 'nada', 'nothing', 'nil', 'no.', 'not today', 'sorry about it', 'not yet', 'patience is a virtue']
        return random.choice(rejects)

    def get_discount():
        try:
            discount = re.findall(make_regex2(), html_source(URL))[0]
            return discount
        except:
            try:
                discount = re.findall(make_regex3(), html_source(URL))[0]
                return discount
            except:
                return 0

    discount=get_discount()
    print('the discount is {}%'.format(discount)) #error handling

    products = [float(i)*(1-float(discount)*.01) for i in re.findall(make_regex(), html_source(URL))]

    quant = len(get_sales(products=products, max_price = 50))

    if quant >0:
        return('yoooo juan lucas there are {} shirts that may fit you, since the discount is {}%'.format(quant, discount))
    else:
        return(rejection())


if __name__ == "__main__":
    print(asics() + '\n' +  jcrew())
