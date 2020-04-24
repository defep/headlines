# -*- coding: utf-8 -*-
import scrapy


class InfobaeRssSpider(scrapy.Spider):
    name = 'infobae_rss'
    allowed_domains = ['infobae.com']
    start_urls = ['https://www.infobae.com/feeds/rss//']

    def parse(self, response):
        for article in response.xpath('//item'):
            yield {
                'title': article.xpath('./title/text()').get(),
                'url': article.xpath('./link/text()').get(),
                'pub_date': article.xpath('./pubDate/text()').get()
            }
