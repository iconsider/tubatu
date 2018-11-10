# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

from tubatu.MyUtils import Utils


class TubatuPipeline(ImagesPipeline):
        pass

#保存Url
class UrlPipeline(object):
    def process_item(self, item, spider):
        #下载url
        self.download_url(item)
        return item

    def download_url(self, item):
        Utils.mkdir(item["urls_path"])
        file = open(item["urls_path"] + "\\源图url.txt", "a", encoding='utf8')
        for url in item["image_urls"]:
            file.write(url + "\n")


# 继承ImagesPipeline，实现下载图片
class ImgPipeline(ImagesPipeline):
    # 发送图片下载请求
    def get_media_requests(self, item, info):
        self.item = self
        for image_url in item['image_urls']:
            self.default_headers['referer'] = image_url
            yield Request(image_url, meta={'item' : item, 'referer' : image_url})

    # 这个方法是在图片将要被存储的时候调用，来获取这个图片存储的路径
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_path = item["image_path"]
        Utils.mkdir(image_path)
        file_name = request.meta['referer'].split("/")[-1]
        return image_path + "\\" + file_name