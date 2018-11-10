# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TubatuItem(scrapy.Item):
    # url文件保存的路径
    urls_path = scrapy.Field()
    # 图片的url地址
    image_urls = scrapy.Field()
    # 图片的存储绝对路径
    image_path = scrapy.Field()
    # 下载成功后返回有关images的一些相关信息
    images = scrapy.Field()

    page_num = scrapy.Field()
