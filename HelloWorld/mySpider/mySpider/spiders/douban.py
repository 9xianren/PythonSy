import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from mySpider.items import DoubanmovieItem
from urllib.parse import urljoin


class Douban(scrapy.spiders.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    # redis_key = 'douban:start_urls'
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        item = DoubanmovieItem()
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        for eachMovie in Movies:
            title = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract() # 多个span标签
            #fullTitle = "".join(title) # 将多个字符串无缝连接起来
            item['title'] = title[0]
            yield item
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        # 第10页是最后一页，没有下一页的链接
        if nextLink:
            nextLink = nextLink[0]
            yield Request(urljoin(response.url, nextLink), callback=self.parse)
