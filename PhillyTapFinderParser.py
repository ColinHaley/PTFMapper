# PhillyTapFinderParser

import sys
import os
import datetime
from BeautifulSoup import BeautifulSoup,SoupStrainer
import urllib2
import httplib2
import PTFEvent

web_page = "http://www.phillytapfinder.com/events/"

http = httplib2.Http()

status, response = http.request(web_page)

# This is the grid.
payload = BeautifulSoup(response, parseOnlyThese=SoupStrainer('div',{'class':'results-grid tall-results'}))

events=[]

for line in payload.findAll('a'):
    event = line.getText('>').split('>')
    link = line.findParent().findAll('a', href=True)[0]['href']
    date = event[2].replace('Event Date: ','')
    title = event[3]
    location = event[4]
    events.append(PTFEvent.PTFEvent(title,location,link,date))
