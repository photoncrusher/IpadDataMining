from os import name
import scrapy
from scrapy.http import HtmlResponse
from crawler.items import IpadItem
import json
import datetime
import re
import requests

class FptSpider(scrapy.Spider):
    name = 'fpt'
    allowed_domains = ['fptshop.com.vn']
    base_url = ['https://fptshop.com.vn/apple/ipad']
    start_url = 'https://fptshop.com.vn'
    def start_requests(self):
        for url in self.base_url:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        product_paths = response.xpath('//div[contains(@class,"product-grid")]/div[contains(@class,"product product-grid__item product--absolute")]/div[contains(@class,"product_img")]/a/@href').getall()
        for product_path in product_paths:
            url = self.start_url + product_path
            yield scrapy.Request(url=url, callback=self.parse_product)
            
    def parse_product(self, response):
        features = response.xpath('//table[@class = "st-pd-table"]').getall()
        data = IpadItem()
        if features != []:
            for feature in features:
                data = IpadItem(
                    name='1',
                )
        if features == []:
            features = response.xpath('//ul[@class = "detail-rm9 active "]').getall()
            for feature in features:
                data = IpadItem(
                    name='2',
                )
        yield data