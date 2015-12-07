# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Save22ProductspidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    url = scrapy.Field()
    title= scrapy.Field()
    description = scrapy.Field()
    retailer_sku_code = scrapy.Field()
    model= scrapy.Field()
    mpn = scrapy.Field()
    sku = scrapy.Field()
    upc = scrapy.Field()
    ean = scrapy.Field()
    currency = scrapy.Field()
    price = scrapy.Field()
    oldprice = scrapy.Field()
    availability = scrapy.Field()
   
    prmo_price = scrapy.Field()
    
