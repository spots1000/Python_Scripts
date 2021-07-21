import scrapy
from scrapy.shell import inspect_response

class GooglespiderSpider(scrapy.Spider):
    name = 'googleSpider'
    allowed_domains = []
    start_urls = ['http://www.homeshoppingmalls.com/robots.txt']

    def parse(self, response):
        
        print("Attemting to process: " + str(response.url))
        print("This is the response we got: " + str(response.status))

        ## Inspect the response
        inspect_response(response, self)

        
        
