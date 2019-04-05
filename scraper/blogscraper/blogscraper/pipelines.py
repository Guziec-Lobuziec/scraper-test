# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re

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
