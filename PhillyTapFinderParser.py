# PhillyTapFinderParser

import sys
import os
import datetime
import BeautifulSoup
import urllib2
import httplib2

web_page = "http://www.phillytapfinder.com/events/"

soup = BeautifulSoup.Soup
strainer = BeautifulSoup.Strainer

http = httplib2.Http()

status, response = http.request(web_page)

for link in BeautifulSoup(response, parseOnlyThese=strainer('ul')):
    print(link)