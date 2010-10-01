import mechanize
import threading
import logging
import datetime

LOG_FILENAME = 'debug.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)


class Hammer(object):
    """Usage: Hammer(url="http://cool.biz", num_swings=10).run()"""
    def __init__(self, url, num_swings=5):
        super(Hammer, self).__init__()
        self.url = url
        self.num_swings = num_swings
        
    def run(self):
        for i in range(self.num_swings):
            Swing(self.url).start()

class Swing(threading.Thread):
    """Used only by Hammer"""
    def __init__(self, url):
        super(Swing, self).__init__()
        self.url = url

    def run(self):
        browser = mechanize.Browser()
        start_time = datetime.datetime.now()
        # open the url
        response = browser.open(self.url).get_data()
        finish_time = datetime.datetime.now()
        timedelta = (finish_time - start_time)
        response_seconds = str(timedelta)
        logging.debug("%s - %s = %s" % (start_time, finish_time, response_seconds))
        logging.debug(response)

    
    
# If you like, you can uncomment the next two lines and invoke Hammer within this file:
# my_url="http://my.site.domain/page"
# Hammer(url=my_url, num_swings=10).run()