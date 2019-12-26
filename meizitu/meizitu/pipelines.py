# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os


class MeizituPipeline(object):
    def process_item(self, item, spider):
        juedui_path = os.path.dirname(os.path.abspath(__file__))
        # img_path = os.path.join(juedui_path, "F:\爬虫(scrapy)\妹子图\%s" % name)
        return item

