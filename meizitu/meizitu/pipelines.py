# -*- coding: utf-8 -*-

import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import re
import time
from urllib import request


class MeizituPipeline(object):
    def process_item(self, item, spider):
        return item


class MZTPipeline(object):
    def __init__(self):
        self.fss = open("meizitu.json", "a", encoding="utf-8",)

    def process_item(self, item, spider):
        tupian = dict(item)
        # img_path = os.path.join(juedui_path, "F:\爬虫(scrapy)\妹子图\%s" % name)
        co = re.compile(r"\d+\w\d+")
        a = co.findall(tupian["img_down"])
        c = re.compile(r"\d+\w")
        d = c.findall(a[1])
        e = [i for i in range(1, 10)]
        page = int(tupian["page"]) + 1
        fi= os.makedirs(r"F:\爬虫(scrapy)\妹子图\%s" %tupian["name"])   # 创建文件夹
        file_root_path = os.path.dirname(os.path.abspath(__file__))  # 获取当前目录的绝对路径
        img_dir_path = os.path.join(file_root_path, r'F:\爬虫(scrapy)\妹子图\%s' % tupian["name"])  # 文件路径
        print(img_dir_path)
        asn = []
        for i in range(1, page):
            if i in e:
                q = str(d[0]) + "0" + str(i)
                urls = re.sub(a[1], q, tupian["img_down"])

            else:
                q = str(d[0]) + str(i)
                urls = re.sub(a[1], q, tupian["img_down"])

            try:

                tpianname = str(tupian["name"]) + str(i) + ".jpg"
                urls = urls
                open = request.build_opener()
                open.addheaders = [("User-Agent",
                                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"),
                                   ("Referer", "https://www.mzitu.com/xinggan/")]
                request.install_opener(open)
                file_down = os.path.join(img_dir_path, tpianname)
                asn.append(urls)
                time.sleep(0.2)
                request.urlretrieve(urls, file_down)
                print("下载完成:   " + tpianname)

            except Exception as es:
                print(es)
        tupian["img_zhu"] = asn
        cont = json.dumps(tupian, ensure_ascii=False, indent=4)
        self.fss.write(cont)