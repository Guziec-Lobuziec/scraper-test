# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from rest.models import WordStatistic


class BlogscraperItem(scrapy.Item):
    content = scrapy.Field()
    author = scrapy.Field()

class WordStatisticItem(DjangoItem):
    django_model = WordStatistic
