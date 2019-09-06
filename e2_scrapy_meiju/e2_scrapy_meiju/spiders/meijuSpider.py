
import scrapy
# 导入需要的item
from e2_scrapy_meiju.items import MeijuItem


# 用来定义spider
class MeijuSpider(scrapy.Spider):

    name = "meiju"
    start_urls = ["https://www.meijutt.com/new100.html"]

    # 重写parse
    def parse(self, response):
        """
        默认已经得到了网页
        反馈的内容用response表示
        其中包含需要的所有数据
        :param response:
        :return:
        """
        # 通过下面xpath, 能够找到所有电源
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')

        print("Movies len: {0}".format(len(movies)))
        for movie in movies:
            """
            每个movie都需要转化成item
            需要先生成一个Item实例对象
            """
            item = MeijuItem()
            item["name"] = movie.xpath('./h5/a/@title').extract()[0]
            item["href"] = movie.xpath('./h5/a/@href').extract()[0]

            # tv 属性可能有问题
            tv = movie.xpath('./span[@class="mjtv"]/text()')

            if len(tv):
                item["tv"] = tv.extract()[0]
            else:
                item["tv"] = ""

            print("Item.name: {0}".format(item["name"]))
            print("Item.href: {0}".format(item["href"]))
            # item只能通过yield返回
            yield item
