# Python 3.8
# Author: TristanCB
# Description: Very basic webscraping examples using scrapy and beautiful soup with requests or urllib3

# web scraping pyhton.org's most recent events using scrapy
### Using scrapy #############################################
import scrapy
from scrapy.crawler import CrawlerProcess
import time

class PythonEventsSpider(scrapy.Spider):
    name = 'pythoneventsspider'
    start_urls = ['https://www.python.org/downloads/',]
    found_events = []
    def parse(self, response):
        # Coming up with valid XPATH: 
        # https://www.softwaretestinghelp.com/xpath-writing-cheat-sheet-tutorial-examples/
        # https://devhints.io/xpath
        # Tip: often in browser console (F12 in chrome) you can "copy XPATH"
        for event in response.xpath('//*[@id="content"]/div/section/div[1]/ol/li'):
            print(event)
            event_details = dict()
            event_details['version'] = event.xpath('span[@class="release-version"]/text()').extract_first()
            event_details['status'] = event.xpath('span[@class="release-status"]/text()').extract_first()
            event_details['start'] = event.xpath('span[@class="release-start"]/text()').extract_first()
            event_details['end'] = event.xpath('span[@class="release-end"]/text()').extract_first()
            event_details['pep'] = event.xpath('span[@class="release-pep"]/a/text()').extract_first()
            self.found_events.append(event_details)

process = CrawlerProcess({ 'LOG_LEVEL': 'DEBUG'})
process.crawl(PythonEventsSpider)
spider = next(iter(process.crawlers)).spider
process.start()
for event in spider.found_events: 
    print(event)

### /Using scrapy ##############################################

### BeautifulSoup and Requests (Heydt, 2018) ###################
import requests
from bs4 import BeautifulSoup

def get_upcoming_events(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    events = soup.find('ul', {'class': 'list-recent-events menu'}).findAll('li')
    for event in events:
        event_details = dict()
        event_details['name'] = event.find('h3').find("a").text
        event_details['location'] = event.find('span', {'class', 'event-location'}).text
        event_details['time'] =  event.find('time').text
        print(event_details)
get_upcoming_events('https://www.python.org/events/python-events/')
### /BeautifulSoup and Requests #################################

### BeautifulSoup and urllib3 (Heydt, 2018) ###################
import urllib3
# from bs4 import BeautifulSoup
def get_upcoming_events_urllib3(url):
    req = urllib3.PoolManager()
    res = req.request('GET', url)
    soup = BeautifulSoup(res.data, 'html.parser')
    events = soup.find('ul', {'class': 'list-recent-events menu'}).findAll('li')
    for event in events:
        event_details = dict()
        event_details['name'] = event.find('h3').find("a").text
        event_details['location'] = event.find('span', {'class', 'event-location'}).text
        event_details['time'] = event.find('time').text
        print(event_details)
get_upcoming_events_urllib3('https://www.python.org/events/python-events/')
### /BeautifulSoup and urllib3 ##################################

### Supplementary #################################

## (Heydt, 2018) ## 
# # Generally recommended to use requests for more advanced features
# import requests
# # builds on top of urllib3's connection pooling
# # session re-uses the same TCP connection if
# # requests are made to the same host
# # see https://en.wikipedia.org/wiki/HTTP_persistent_connection for details
# session = requests.Session()
# # You may pass in customized cookie
# r = session.get('http://httpbin.org/get', cookies={'my-cookie': 'browser'})
# print(r.text)
# # '{"cookies": {"my-cookie": "test cookie"}}'
# # Streaming is another nifty feature
# # From http://docs.python-requests.org/en/master/user/advanced/#streaming-requests
# # copyright belongs to request.org
# r = requests.get('http://httpbin.org/stream/20', stream=True)

# A simple download bar for visual feedback
def download(url, filename):
    """
    Taken from: https://stackoverflow.com/questions/15644964/python-progress-bar-and-downloads
    """
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)
                sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')


### References #################################################
# Heydt, Michael. __Python Web Scraping Cookbook : Over 90 Proven Recipes to Get You Scraping with Python, Microservices, Docker, and Aws.__ Packt Publishing, 2018.
### /References ################################################

