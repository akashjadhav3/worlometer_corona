# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus//']

    def parse(self, response):
        title = response.xpath("//h3/text()").get()  # return title of h3 tag
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # absolute_url = f"https://www.worldometer.info{link}" //manualy


            yield response.follow(url=link) # url generate automaticaly

        # yield{
        #     'country_name':name,
        #     'country_link':link
        # }
