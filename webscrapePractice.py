#functions are built into a toolbox/package called a standard library
#to pull an entire kit, use the 'import' command - here we using [urllib2] package - visit sites with python

import urllib2 

#can also import specific tools from inside a toolkit/package by using 'from' command

from urllib2 import urlopen
urlopen("http://www.python.org")

#import statements always at the top of the script


#step 1: inspect source - webpage - a table with data you need
#step 2: find a pattern or identifier in the code - 
#best case, we can see [id - unique id] or [class - specific type of item] already assigned to elements we wana extract

#e.g, extracting an html table class

#import requests library and download webpage

import requests

url = 'https://www.nhl.com/standings/2018/wildcard'
response = requests.get(url)
html = response.content
print html

#should spit out html of the webpage
#next import BeautifulSoup html parsing lib and feed to page

import requests 
from BeautifulSoup import BeautifulSoup

url = 'https://www.nhl.com/standings/2018/wildcard'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
print soup.prettify()

