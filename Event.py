import datetime

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