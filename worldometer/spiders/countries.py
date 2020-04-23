# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/coronavirus//']

    def parse(self, response):
        title = response.xpath("//h3/text()").get()  # return title of h3 tag
        countries = response.xpath("//td/a/text()").getall() #return all countries List

        yield{
            'title':title,
            'countries':countries
        }
