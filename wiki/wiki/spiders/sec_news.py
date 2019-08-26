# -*- coding: utf-8 -*-
import scrapy
import copy
from ..items import WikiItem

class SecNewsSpider(scrapy.Spider):
    name = 'sec-news'
    allowed_domains = ['wiki.ioin.in']
    start_urls = ['http://wiki.ioin.in/']

    def parse_post_url(self, response):
        item = response.meta['item']
        item['real_url'] = response.css('#detail > blockquote > p.url.wrap::text').get().strip()
        return item

    def parse_url(self, response):
        articles = response.xpath('/html/body/div[1]/table/tbody/tr')

        item = WikiItem()
        for article in articles:
            item['title'] = article.css('a::text').get().strip()
            item['link'] =  'http://wiki.ioin.in' + article.css('a::attr(href)').get().strip()
            item['data_time']  = article.css('td::text').get().strip()
            item['article_type'] = article.css('td:nth-child(3) > a::text').get().strip()
            item['click'] = article.css('td.text-center > a::text').re('(.*)/')[0].strip()

            post_url = 'http://wiki.ioin.in' + article.xpath('td[4]/a/@href').get().strip()
            yield scrapy.Request(post_url, callback=self.parse_post_url,
                meta={'item':copy.deepcopy(item)})

    def parse(self, response):
        count = response.xpath('/html/body/div[1]/ul/li[last()-1]/a/text()').get()
        for i in range(1, int(count)+1):
            url = response.url + "page-" + str(i)
            yield scrapy.Request(url, callback=self.parse_url)
