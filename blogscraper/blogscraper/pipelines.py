# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import copy
from rest.models import AuthorStatistic, GloballStatistic, Author, StatsVersion, Word
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

    new_version = None

    def open_spider(self, spider):
        self.new_version = StatsVersion.objects.create(ready=False)

    def close_spider(self, spider):
        StatsVersion.objects.filter(ready = True).delete()
        self.new_version.ready = True
        self.new_version.save()

    def process_item(self, item, spider):

        author = None

        if item.get('author'):
            author_in_db = Author.objects.get_or_create(
                url=item['author'].lower().replace(" ",""),
                defaults={'full_name': item['author']}
            )[0]

        if item.get('content'):
            stats = defaultdict(int)
            for k in item['content']:
                stats[k] += 1

            words_in_db = {k: Word.objects.get_or_create(word_of_interest = k)[0]
                      for k in stats.keys()}

            if(author_in_db):
                for k,v in self.prepair_author_stats(author_in_db,stats).items():
                    AuthorStatistic.objects.update_or_create(
                        word = words_in_db[k],
                        author = author_in_db,
                        version = self.new_version,
                        defaults = {'occurance_count': v}
                    )

            for k,v in self.prepair_global_stats(stats).items():
                GloballStatistic.objects.update_or_create(
                    word = words_in_db[k],
                    version = self.new_version,
                    defaults = {'occurance_count': v}
                )

        return stats

    def prepair_stats(self, stats, query):

        cp = copy.deepcopy(stats)
        for record in query:
            cp[record.word.word_of_interest] += record.occurance_count

        return cp


    def prepair_author_stats(self, author, stats):

        return self.prepair_stats(
            stats = stats,
            query = AuthorStatistic.objects \
            .filter(author__url = author.url) \
            .filter(word__word_of_interest__in = stats.keys()) \
            .filter(version__version_number = self.new_version.version_number)
        )

    def prepair_global_stats(self, stats):

        return self.prepair_stats(
            stats = stats,
            query = GloballStatistic.objects \
            .filter(word__word_of_interest__in = stats.keys()) \
            .filter(version__version_number = self.new_version.version_number)
        )
