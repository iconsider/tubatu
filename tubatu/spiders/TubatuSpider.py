import time

import scrapy

from scrapy import Request
from scrapy.utils.project import get_project_settings

from tubatu.items import TubatuItem


class TubatuSpider(scrapy.spiders.Spider):
    #处理404的情况
    handle_httpstatus_list = [404]
    name = "tubatu"
    allowed_domains = ["to8to.com"]
    start_urls = [
        "http://gz.to8to.com/zs/8708815/case/400000.html"
        # "http://gz.to8to.com/zs/8708815/case/484240.html"
    ]



    def parse(self, response):
        print("-----------------------------------")
        url_base_path = "Z:\\urls\\"
        image_base_path = get_project_settings().get("IMAGES_STORE")
        page_num = response.url.split("/")[-1].replace(".html", "")
        print("status: %s" % response.status)

        image_urls = response.css('.desc-content img[data-original]::attr(data-original)').extract()
        item = TubatuItem()
        item["urls_path"] = "%s%s" % (url_base_path, page_num)
        item["image_path"] = "%s%s" % (image_base_path, page_num)
        item["image_urls"] = image_urls
        item["page_num"] = page_num
        yield item

        #防止过快被禁
        time.sleep(3)
        nextPageUrl = "http://gz.to8to.com/zs/8708815/case/%s.html" % "%06d" % (int(page_num) + 1)
        yield Request(url=nextPageUrl, callback=self.parse)


