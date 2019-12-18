# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class E3QqPipeline(object):
    def process_item(self, item, spider):
        return item


class QQPipeline(object):
    """
    假设数据需要写入文件
    那么在什么时候关闭,打开文件
    """
    def __init__(self):
        self.file = open('qq.json', "a", encoding="utf-8")

    def process_item(self, item, spider):
        # item 可以直接转换成字典
        # print(type(item))
        content = json.dumps(dict(item), ensure_ascii=False, indent=4)
        self.file.write(content)
        # with open("qq.json", "w")as f:
        #     f.write(dict(item))
        return item


    def close_spider(self, spider):
        self.file.close()
