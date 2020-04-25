# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.shell import inspect_response
class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        # title = response.xpath("//h3/text()").get()  # return title of h3 tag
        countries = response.xpath("//td/a")
        for country in countries:
            name_country = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
            # absolute_url = f"https://www.worldometer.info{link}" //manualy
            yield response.follow(url='https://www.worldometers.info/coronavirus/country/us/', callback=self.parse_country,meta = {'country_name':'usa'}) # url generate automaticaly
    
    def parse_country(self,response):
        inspect_response(response, self)
        country_name = response.request.meta['country_name']
        rows = response.xpath("//table[@id='usa_table_countries_today']/tbody/tr[position()>1]")
        
        for row in rows:
            city = row.xpath(".//td[1]/text()").get()
            total_cases = row.xpath(".//td[2]/text()").get()
            yield {
                'country_Name':country_name,'city':city, 'total_cases':total_cases
            }
