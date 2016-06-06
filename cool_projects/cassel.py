import requests
import sys, os
import json
import re
import json

def cassel():
   URL = 'https://cassel-z.firebaseio.com/Customers/2243559207.json'

   r = requests.get(URL).json()
   return r

def cassel2():
   URL = 'https://cassel-z.firebaseio.com/Teams/Wolverines.json'

   r = requests.get(URL).json()

   return r

def cassel3(URL):
   URL = 'https://cassel-z.firebaseio.com/Teams/Wolverines.json'

   r = requests.get(URL).json()
   return r

if __name__ == "__main__":
    print(cassel())
