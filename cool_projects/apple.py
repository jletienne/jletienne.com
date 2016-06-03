import requests
import sys, os
import json
import re



def applebot():
   URL = 'http://www.9to5mac.com'

   def html_source(URL):
       return requests.get(URL).text

   def make_regex():
       ips = ['<h1 class="post-title">(.*?)</h1>']
       products = "".join(ips)
       return products
   def make_regex2():
       ips = ['">(.*?)</a>']
       products = "".join(ips)
       return products

   apple = re.findall(make_regex(), html_source(URL))
   apple2 = re.findall(make_regex2(), "".join(apple))
   return apple2
   
if __name__ == "__main__":
    print(applebot())
