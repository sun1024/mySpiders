# -*- coding: utf-8 -*-
import scrapy

from ..items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        all_teachers = response.xpath('/html/body/div[1]/div[5]/div[2]/div[4]/ul/li')

        item = MyspiderItem()
        for teacher in all_teachers:
            item['name'] = teacher.css("h3::text").get()
            item['title'] = teacher.css("h4::text").get()
            item['info'] = teacher.css("p::text").get()
            yield item
