
from urllib import request

import scrapy
from lxml import etree
from meizitu.items import MeizituItem


class Meizituspider(scrapy.Spider):
    name = "meizitu"

    allowed_domains = ["mzitu.com"]
    start_urls = []

    for i in range(1, 2):
        url = "https://www.mzitu.com/page/%s" % i
        start_urls.append(url)


    def parse(self, response):

       zhuye_url = []
       content = response.body.decode("utf-8")
       data = etree.HTML(content)

       for each in data.xpath("//div/ul[@id='pins']/li"):
           zhuyemian = each.xpath(".//a/@href")[0]
           zhuye_url.append(zhuyemian)

       for each_zhu_url in zhuye_url:
       # each_zhu_url = random.choice(zhuye_url)
       # print(each_zhu_url)

           headers = {
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400"
           }
           rsp = request.Request(each_zhu_url, headers=headers)
           rep = request.urlopen(rsp)
           html = rep.read().decode()
           html = etree.HTML(html)
           pages = html.xpath("//div[2]/div[1]/div[4]/a[5]/span/text()")[0]
           names = html.xpath("//div[@class='content']/h2/text()")[0]
           imgsss = html.xpath("//div[@class='main-image']/p/a/img/@src")[0]

           item = MeizituItem()
           item["name"] = names
           item["page"] = pages
           item["img_down"] = imgsss
           print(imgsss)
           item["img_zhu"] = zhuye_url

           yield item