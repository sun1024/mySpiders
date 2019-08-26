# -*- coding: utf-8 -*-
import scrapy

from ..items import NvshensItem

class LiufeierSpider(scrapy.Spider):

	name = "liufeier"
	allowed_domains = ["www.nvshens.net"]
	start_urls = [
        "https://www.nvshens.net/girl/19705/album/",
        ""
        ]


	def parse_info(self,response):
		nvshens_info = response.meta['nvshens_info']
		nvshens_info['name'] = response.xpath('//div[@class="albumTitle"]/h1/text()').extract()
		nvshens_info['img'] = response.xpath('//div[@class="gallery_wrapper"]/ul//img/@src').extract()
		return nvshens_info


	def parse_links(self,response):    #每个相册中的图片URL提取
		parse_url = response.xpath('//div[@id="pages"]//a/@href').extract()
		url_host = 'https://' + response.url.split('/')[2]
		parse_url_tmp = []
		nvshens_info = NvshensItem()
		for i in parse_url:
			if i not in parse_url_tmp:
				parse_url_tmp.append(i)
		for x in parse_url_tmp:
			url_format = "{}{}".format(url_host,x)
			yield scrapy.Request(url_format,meta={'nvshens_info':nvshens_info},callback=self.parse_info)


	def parse(self, response):
		url = 'https://www.nvshens.net{}'
		base_link = response.xpath('//div[@class="res_infobox clearfix"]//li//a/@href').extract()  #抓取相册全部URL并去重复，然后拼接URL
		last_tmp = []
		for x in base_link:
			if x not in last_tmp:
				last_tmp.append(x)
		for i in last_tmp:
			yield scrapy.Request(url.format(i),callback=self.parse_links)