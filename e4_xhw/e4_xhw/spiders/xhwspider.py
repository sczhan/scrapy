import scrapy
from e4_xhw.items import XiaohuaItem
from urllib import request

class XiaohuaSpider(scrapy.Spider):
    name = "xiaohua"
    allowed_domains = ["xiaohuar.com"]
    page = 0
    start_urls = ["http://www.xiaohuar.com/list-1-0.html"]

    def parse(self, response):
        bookmarks = response.xpath('//div[@class="item_t"]')
        for bm in bookmarks:
            item = XiaohuaItem()
            title = bm.xpath('.//div[@class="title"]/span/a//text()').extract()[0]
            print(title)
            href = bm.xpath('.//div[@class="img"]/a/@*').extract()[0]
            print(href)
            src = bm.xpath('.//div[@class="img"]/a//@src').extract()[0]
            print(src)
            name = bm.xpath('.//div[@class="img"]/span//text()').extract()[0]
            print(name)
            src = str(src)
            if src.endswith(".jpg"):
                image_url = "http://www.xiaohuar.com" + src
                print(image_url)
                # src = src.replace(".php", ".jpg")
                if src.endswith(".jpg")and src.startswith("http"):
                    image_url = src
                    print(image_url)
                # else:
                #     image_url = "http://www.xiaohuar.com" + src
                #     print(image_url)
            item["title"] = title
            item["href"] = href
            item["src"] = src
            item["image_url"] = image_url
            item["name"] = name

            yield item
            # 图片为http://www.xiaohuar.com/s-1-2101.html#p1
        self.page += 1
        if self.page < 2:
            url = "http://www.xiaohuar.com/list-1-" + str(self.page) + ".html"
            yield scrapy.Request(url=url, callback=self.parse)
# class XiaohuaSpider(scrapy.Spider):
#     name = 'xiaohua'
#     allowed_domains = ['www.xiaohuar.com']
#     # 基础url
#     url = 'http://www.xiaohuar.com/list-1-'
#     # 爬取的起始页
#     page = 0
#     # 爬取的起始url
#     start_urls = ['http://www.xiaohuar.com/hua/list-1-0.html']
#
#     # 定义的方法，注意这个方法名不能修改，传入的参数也不能修改，否则会出错
#     def parse(self, response):
#         # print(100)
#         # 解析所有校花，获取指定内容
#         div_list = response.xpath('//div[@class="item masonry_brick"]')
#         print(div_list)
#         # 遍历上面所有的div，找到指定的内容即可
#         item = XiaohuaItem()
#         yield item