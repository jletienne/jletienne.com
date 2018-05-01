import requests
import random

def request_movie():
    r = requests.get('https://raw.githubusercontent.com/mastercbf/waldy/master/dicksflicks.json')
    filmNumber = random.randrange(0,len(r.json()))
    return r.json()[filmNumber]

def search_movie(movie='Get Shorty'):
    r = requests.get('https://raw.githubusercontent.com/jletienne/jletienne.com/master/static/films.json')
    return r.json(movie)

if __name__ == '__main__':
    request_movie()
