import scrapy
from scrapy.http import HtmlResponse
import json
import datetime
import re
import requests

class fptSpider(scrapy.Spider):
    name = 'fptshop'
    def start_requests(self):
        allowed_domains = ['fptshop.com.vn']
        base_url = ['https://fptshop.com.vn/apple/ipad']
        for url in base_url:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response, *args, **kwargs):
        products = response.xpath('//div[contains(@class,"product-grid")]/div[contains(@class,"product product-grid__item product--absolute")]/div[contains(@class,"product_img")]/a/@href').getall()
        for product in products:
            yield{
                'url':product
            }