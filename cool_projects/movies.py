import requests
import random

def request_movie():
    r = requests.get('https://raw.githubusercontent.com/mastercbf/waldy/master/dicksflicks.json')
    filmNumber = random.randrange(0,len(r.json()))
    return r.json()[filmNumber]


if __name__ == '__main__':
    request_movie()
