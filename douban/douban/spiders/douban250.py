# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanItem

class Douban250Spider(scrapy.Spider):
    name = 'douban250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        movies = response.xpath('//*[@id="content"]/div/div[1]/ol/li')

        item = DoubanItem()

        for movie in movies:
            item['name'] = movie.css('div.pic > a > img::attr(alt)').get()
            item['score'] = movie.css('span.rating_num::text').get()
            yield item

        next_page = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first()

        if next_page:
            yield response.follow(next_page, callback=self.parse)
