import mechanize
import threading
import logging
import datetime

LOG_FILENAME = 'debug.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)


class Swing(threading.Thread):
    """docstring for Swing"""
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
        response_ms = timedelta.microseconds/1000
        logging.debug("%s - %s" % (start_time, response_ms))
        


class Hammer(object):
    """Usage: Hammer(url="http://cool.biz", num_swings=10).run()"""
    def __init__(self, url, num_swings=5):
        super(Hammer, self).__init__()
        self.url = url
        self.num_swings = num_swings
        
    def run(self):
        for i in range(self.num_swings):
            Swing(self.url).start()
    

Hammer(url="http://kyle.tbxing.com/frontend_dev.php/test/index", num_swings=20).run()