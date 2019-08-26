# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib.request
import datetime
import hashlib

class NvshensPipeline(object):
    def process_item(self, item, spider):
        x = 0
        for img_link in item['img']:
            img_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            urllib.request.urlretrieve(img_link, '{}{}.jpg'.format(img_time, x))
            x += 1
        return item