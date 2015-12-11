# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AfycrawlItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    primary_image_url = scrapy.Field()
    sku = scrapy.Field()
    currency = scrapy.Field()
    outOfStock = scrapy.Field()
    oldprice = scrapy.Field()
    description = scrapy.Field()
    crawltime = scrapy.Field()