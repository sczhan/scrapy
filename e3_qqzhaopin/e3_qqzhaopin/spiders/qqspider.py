import datetime
import json

import scrapy

from e3_qqzhaopin.items import QQItem


def shijianjie():
    import time
    a = datetime.datetime.now()
    b = str(int(time.mktime(a.timetuple())))
    c = str("%06d" % a.microsecond)[0:3]
    time = str(b) + str(c)
    return time

a = str(shijianjie())


class QQSpider(scrapy.Spider):

    name = "qq"

    # 设置只能爬取腾讯域名的信息
    allowed_domains = ["tencent.com"]

    start_urls = ["https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1576654934354&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn"]
    # start_urls = []
    # for i in range(1, 10):
    #     url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=" + str(shijianjie()) + "&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=" + str(i) + "&pageSize=10&language=zh-cn&area=cn"
    #     start_urls.append(url)
    # print(start_urls)

    def parse(self, response):
        """
        下载的结果自动放到response内存储
        :param response:
        :return:
        """
        content = response.body.decode('utf-8')
        # json字符串转换为python格式
        # print(content)
        data = json.loads(content, encoding="utf-8")
        # print(data)
        urlss = []
        for each in data["Data"]["Posts"]:
            # print(each)
            # 对于得到的每一个工作信息内容
            # 把数据封装入相应的item内
            item = QQItem()
            name = each["RecruitPostName"]
            print(name)
            detailLink = each["PostURL"]
            positionInfo = each["Responsibility"]
            workLocation = each["LocationName"]

            item["name"] = name
            item["detailLink"] = detailLink
            item["positionInfo"] = positionInfo
            item["workLocation"] = workLocation
            yield item

    #         # print(type(item))
    #
    #         # 处理继续爬取的链接
    #         # 通过得到当前页, 提取数字,把数字加10, 替换成原来的数字,就是下一个页面地址
    #         # 提取当前页的数字
    #         # curpage = re.search("pageIndex=\d", response.url)
    #         # print(11)
    #         # print(curpage)
    #         # # 生成下一页的数字值
    #         # page = int(curpage) + 10
    #         # 生成下一页url
    #
    #
        for i in range(2, 5):
              urls = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=" + \
                     str(a)+ "&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=" + \
                     str(i) + "&pageSize=10&language=zh-cn&area=cn"
              yield scrapy.Request(urls, callback=self.parse, )
    #     # print("*"*20, urlss,  "#"*20, str(times))
    #     #
    #     # # 把地址通过yield返回
    #     # # 注意callback的写法
    #         yield scrapy.Request(urls, callback=self.parse,)
    #     yield item
    #     # # 获取的item提交给pipeline
