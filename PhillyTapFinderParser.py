# PhillyTapFinderParser

import sys
import os
import datetime
from BeautifulSoup import BeautifulSoup,SoupStrainer
import urllib2
import httplib2


class Event:

    title = ""
    location = ""
    hyperlink = ""
    date = datetime.date.today()

    def __init__(self, Title, Location, HyperLink, Date):
        title = Title
        location = Location
        hyperlink = HyperLink
        date = Date

def create_event():
    return 0


web_page = "http://www.phillytapfinder.com/events/"

http = httplib2.Http()

status, response = http.request(web_page)

# This is the grid.
payload = BeautifulSoup(response, parseOnlyThese=SoupStrainer('div',{'class':'results-grid tall-results'}))
for line in payload.findAll('a'):
    a = line.get('href')
    b = line.get('title')
    print (a + "" + b)
    -#span stuff should go under findAll('a')
spans = payload.findAll('span')
spans[0].findAll('span')[0].getText('>')
for x in spans[0].findAll('span'):
    x.getText('>')
