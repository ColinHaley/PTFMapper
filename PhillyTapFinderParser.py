import sys
import os
import datetime
from BeautifulSoup import BeautifulSoup,SoupStrainer
import urllib2
import httplib2
import PTFEvent

web_page = "http://www.phillytapfinder.com/events/"

def get_events():
    events = []
    http = httplib2.Http()
    status, response = http.request(web_page)
    payload = BeautifulSoup(response, parseOnlyThese=SoupStrainer('div',{'class':'results-grid tall-results'}))

    for line in payload.findAll('a'):
        event = line.getText('>').split('>')
        link = line.findParent().findAll('a', href=True)[0]['href']
        date = event[2].replace('Event Date: ','')
        title = event[3]
        location = event[4]
        events.append(PTFEvent.PTFEvent(title,location,link,date))

    return events