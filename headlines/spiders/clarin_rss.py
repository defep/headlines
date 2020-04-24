# -*- coding: utf-8 -*-
import scrapy


class ClarinRssSpider(scrapy.Spider):
    name = 'clarin_rss'
    allowed_domains = ['https://www.clarin.com/rss/lo-ultimo/']
    start_urls = [
        'https://www.clarin.com/rss/lo-ultimo/',
        'https://www.clarin.com/rss/politica/',
        'https://www.clarin.com/rss/mundo/',
        'https://www.clarin.com/rss/sociedad/',
        'https://www.clarin.com/rss/policiales/',
        'https://www.clarin.com/rss/ciudades/'
    ]

    def parse(self, response):
        for article in response.xpath('//item'):
            yield {
                'title': article.xpath('./title/text()').get(),
                'url': article.xpath('./link/text()').get(),
                'pub_date': article.xpath('./pubDate/text()').get()
            }

