from os import name
import scrapy
from scrapy.http import HtmlResponse
from crawler.items import IpadItem
import json
import datetime
import re
import requests

class UscomSpider(scrapy.Spider):
    name = 'uscom'
    allowed_domains = ['uscom.vn']
    base_url = ['http://uscom.vn/']
    start_url = 'http://uscom.vn/'
    list_url = []
    def start_requests(self):
        for index in range(1,6):
            new_url = 'https://uscom.vn/ipad1_p'+str(index)
            self.list_url.append(new_url)
        for url in self.list_url:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        product_paths = response.xpath('//div[(@class="prd-info")]/h5/a/@href').getall()
        for product_path in product_paths:
            url = product_path
            yield scrapy.Request(url=url, callback=self.parse_product)
            
    def parse_product(self, response):
        features = response.xpath('//table[@class="table table-bordered table-condensed table-striped table-hover"]').getall()
        data = IpadItem()
        if features != []:
            for feature in features:
                data = IpadItem(
                    name='1',
                )
        yield data