import scrapy
from scrapy.spider import CrawlSpider,Rule
import datetime
import re
from scrapy.linkextractors import LinkExtractor
from afycrawl.items import AfycrawlItem
class Afyspider(CrawlSpider):
    
    name = "AFYcrawl"
    allowed_domains = ["www.allforyou.sg"]
    start_urls = [
        "https://www.allforyou.sg/"]
    linkss=[]
    
    rules=[	Rule(LinkExtractor( allow = (r'.+/',),deny =(r'Feedback',r'.+?filter.+',r'.+forum.+',r'.+signin.+','.+blog.+')),callback='parse_grid_contents',follow=True)
      
          
          ]
    lnkk=[]
    def parse_grid_contents(self,response):
        print "got in hsadfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffere"
        for r in response.xpath('//html'):
             
            item = AfycrawlItem()
            print "got in here"
            
            for lnk in response.xpath('//div[@class="prod-data"]'):
                if lnk.xpath('@data-newprodid'):
                    if lnk.xpath('@data-newprodid').extract() not in self.linkss:
                         now = datetime.datetime.now()
                         self.linkss.append(lnk.xpath('@data-newprodid').extract())
                         items = AfycrawlItem()
                         items['title'] = lnk.xpath('@data-name').extract()
                         items['price'] = lnk.xpath('@data-price').extract()
                         items['sku'] = lnk.xpath('@data-newprodid').extract()
                         items['primary_image_url'] = lnk.xpath('@data-imgurl').extract()
                         items['currency'] = 'SGD'
                         items['outOfStock'] = lnk.xpath('@data-outofstock').extract()
                         items['oldprice'] = lnk.xpath('@data-oldprice').extract()
                        
                         items['crawltime'] =now.strftime("%Y-%m-%d %H:%M:%S")
                         yield items
  