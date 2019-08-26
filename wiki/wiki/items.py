# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WikiItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field() # 标题
    link = scrapy.Field() # 链接 
    real_url = scrapy.Field() # 真实链接
    data_time = scrapy.Field() # 时间
    article_type = scrapy.Field() # 文章类别
    click = scrapy.Field() # 点击

