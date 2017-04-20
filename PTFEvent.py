import datetime

class PTFEvent:

    title = None
    location = None
    hyperlink = None
    date = None

    def __init__(self, Title, Location, HyperLink, Date):
        self.title = Title
        self.location = Location
        self.hyperlink = HyperLink
        self.date = Date