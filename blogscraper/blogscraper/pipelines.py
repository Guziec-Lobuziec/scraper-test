# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
from blogscraper.items import WordStatisticItem
from collections import defaultdict

class PrettifyPipeline(object):

    only_numbers = re.compile('^(?:-|\+)?\d+(?:\.\d+)?%?$')
    only_whitespaces = re.compile('^\s*$')
    separators = re.compile('(?:(?:\s+-\s+)|\s|(?:\.\s+)|(?:,\s+)|(?:\?\s+)|\(|\)|(?:\s+&\s+))+')
    non_alphanumerics = re.compile('(:?^\W+)|(:?\W+$)',
                                   re.MULTILINE)
    urls_reg = re.compile('https?://.*')

    def process_item(self, item, spider):

        if not (item.get('content') and item.get('author')):
            raise DropItem("No content and author in %s" % item)

        if item.get('content'):
            item['content'] = [self.non_alphanumerics.sub('',y)
                                for x in item['content']
                                if not (self.only_whitespaces.match(x))
                                for y in self.separators.split(self.non_alphanumerics.sub('',x))
                                if y
                                if not (self.only_numbers.match(y))
                                if not (self.urls_reg.match(y))]

        return item


class StopWordsPipeline(object):

    def process_item(self, item, spider):
        return item


class PersistancePipeline(object):
    """docstring for PersistancePipeline."""

    def process_item(self, item, spider):

        if item.get('content'):
            stats = defaultdict(int)
            for k in item['content']:
                stats[k] += 1


            for record in WordStatisticItem.django_model.objects.filter(word_of_intrest__in = stats.keys()):
                    stats[record.word_of_intrest] += record.occurance_count

            for k,v in stats.items():
                WordStatisticItem(
                    word_of_intrest = k,
                    occurance_count = v
                ).save()


        return item
