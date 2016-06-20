# PhillyTapFinderParser

import sys
import os
import datetime
from BeautifulSoup import BeautifulSoup,SoupStrainer
import urllib2
import httplib2

web_page = "http://www.phillytapfinder.com/events/"

http = httplib2.Http()

status, response = http.request(web_page)

unordered_lists = BeautifulSoup(response, parseOnlyThese=SoupStrainer('ul'))

for items in unordered_lists:
    if 'href=/event/'






class Event:

    title = ""
    location = ""
    hyperlink = ""
    date = datetime.date.today()

    def __init__(self):
        # something

