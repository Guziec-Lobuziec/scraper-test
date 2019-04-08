# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from blogscraper.items import BlogscraperItem


class TeonitewordstatsSpider(CrawlSpider):
    name = 'teonitewordstats'
    allowed_domains = ['teonite.com']
    start_urls = ['https://teonite.com/blog/']

    rules = (
        Rule(LinkExtractor(allow=('(/page/\d+/)?'), restrict_css=('.older-posts'))),
        Rule(LinkExtractor(deny=('/tag/.*') ,restrict_css=('.post')), callback='parse_item')
    )

    def parse_item(self, response):
        post = response.xpath('//article')
        item = BlogscraperItem(
            content = (post.xpath('./header/h1//text()').getall()
                        + post.css('.post-content').xpath('.//text()').getall()),
            author = post.xpath('./footer').css('.author').xpath('.//h4//text()').get()
        )
        return item
