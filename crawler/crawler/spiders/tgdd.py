from os import name
import scrapy
from scrapy.http import HtmlResponse
from crawler.items import IpadItem
import json
import datetime
import re
import requests

class TgddSpider(scrapy.Spider):
    name = 'tgdd'
    allowed_domains = ['thegioididong.com']
    start_url = 'https://www.thegioididong.com'
    base_url = ['https://www.thegioididong.com/may-tinh-bang-apple-ipad']

    def start_requests(self):
        for url in self.base_url:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        product_paths = response.xpath('//li[@class=" item ajaxed"]/a/@href').getall()
        for product_path in product_paths:
            url = self.start_url + product_path
            yield scrapy.Request(url=url, callback=self.parse_product)
            
    def parse_product(self, response):
        features = response.xpath('//div[@class="parameter-all"]').getall()
        data = IpadItem()
        if features != []:
            for feature in features:
                data = IpadItem(
                    name='1',
                )
        yield data
