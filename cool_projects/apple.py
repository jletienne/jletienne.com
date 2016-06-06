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
   apple2 = re.findall(make_regex2(), "".join(apple))[:-1]
   x = "|".join(apple2)
   x = x.replace('&nbsp;', ' ')
   x = x.replace('&amp;', '&')
   x = x.replace('&#8243;', '"')
   x = x.replace('&#8217;', "\\'")

   return x

if __name__ == "__main__":
    print(applebot())
