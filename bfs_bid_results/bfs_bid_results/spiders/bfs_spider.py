         #'http://www4.honolulu.gov/bfspurchasingbids/main/vueCBids.asp?sProjId=201366002',
            #'http://www4.honolulu.gov/bfspurchasingbids/main/vueBidResults.asp?sType=C',

import scrapy

#import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.url import url_query_cleaner


def process_links(links):
    for link in links:
        link.url = url_query_cleaner(link.url)
        yield link


class BidResultsCrawler(CrawlSpider):
    name = 'bid_results'
    allowed_domains = ['www4.honolulu.gov/bfspurchasingbids/main']
    start_urls = ['http://www4.honolulu.gov/bfspurchasingbids/main/vueBidResults.asp?sType=C']
#    rules = (Rule(LinkExtractor()),)
    rules = (Rule(LinkExtractor(),callback='parse_item'),)

   # rules = (
   #     Rule(
    #        LinkExtractor(
                #deny=[
                    #re.escape('https://www.imdb.com/offsite'),
                    #re.escape('https://www.imdb.com/whitelist-offsite'),
                #],
    #        ),
    #        process_links=process_links,
    #        callback='parse_item',
    #        follow=True
    #    ),
    #)

    def parse_item(self, response):
        return {
            'url': response.url
            #'metadata': extruct.extract(
            #    response.text,
            #    response.url,
            #    syntaxes=['opengraph', 'json-ld']
            #),
        }
