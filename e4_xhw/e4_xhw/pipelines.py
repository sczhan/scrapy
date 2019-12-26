# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import urllib.request
import os


class E4XhwPipeline(object):
    def process_item(self, item, spider):
        return item


class XiaohuaPipeline(object):

    def __init__(self):
        self.file = open("xiaohua.json","a", encoding="utf-8")

    def process_item(self, item, spider):
        str = json.dumps(dict(item), ensure_ascii=False, indent=4)
        # str =str + "\n"
        self.file.write(str)
        tupian = dict(item)
        file_root_path = os.path.dirname(os.path.abspath(__file__))  # 获取当前目录的绝对路径
        img_dir_path = os.path.join(file_root_path, r'F:\爬虫(scrapy)\校花网图片')  #文件路径
        filename = tupian["name"] + ".jpg"  # 图片名称
        filepath = os.path.join(img_dir_path, filename)   # 下载路径和图片名称
        urllib.request.urlretrieve(tupian["image_url"], filepath)  # 下载图片

    def close_spider(self, spider):
        self.file.close()
