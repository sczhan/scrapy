
import re

import scrapy

from e3_qqzhaopin.items import QQItem


class QQSpider(scrapy.Spider):

    name = "qq"

    # 设置只能爬取腾讯域名的信息
    allowed_domains = ["tencent.com"]

    start_urls = ["https://careers.tencent.com/search.html?&start=0#a"]


    def parse(self, response):
        """
        下载的结果自动放到response内存储
        :param response:
        :return:
        """
        print("还未执行函数")
        content = response.body.decode('utf-8')
        # json字符串转换为python格式
        print(content)
        # data = json.loads(content, encoding="gbk")
        # print()
        print(response.xpath('//tr[@class="even"] | //tr[@class="odd"]'))
        for each in response.xpath('//div[@class="recruit-list"]'):
            # 对于得到的每一个工作信息内容
            # 把数据封装入相应的item内
            item = QQItem()
            print("77777777777777777")
            name = each.xpath("./a/h4/text()").extract()[0]
            print("3")
            detailLink = each.xpath("./td[1]/a/@href").extract()[0]
            positionInfo = each.xpath("./td[2]/text").extract()[0]
            workLocation = each.xpath("./td[4]/text()").extract()[0]

            item["name"] = name.encode("utf-8")
            item["detailLink"] = detailLink.encode("utf-8")
            item["positionInfo"] = positionInfo.encode("utf-8")
            item["workLocation"] = workLocation.encode("utf-8")


            # 处理继续爬取的链接
            # 通过得到当前页, 提取数字,把数字加10, 替换成原来的数字,就是下一个页面地址
            # 提取当前页的数字
            curpage = re.search("\d+", response.url).group(1)
            # 生成下一页的数字值
            page = int(curpage) + 10
            # 生成下一页url
            url = re.sub("\d", str(page), response.url)

            # 把地址通过yield返回
            # 注意callback的写法
            yield scrapy.Request(url, callback=self.parse)

            # 获取的item提交给pipeline
            yield item