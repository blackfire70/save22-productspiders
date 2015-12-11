import scrapy
from scrapy.spider import CrawlSpider, Rule
import datetime

from allforyou_sg.items import AllforyouSgItem
class AllForYouCrawler(scrapy.Spider):
    
    name = "AFY"
    allowed_domains = ["www.allforyou.sg"]
    start_urls = [
        "https://www.allforyou.sg/"]
    linkss=[]
    now = datetime.datetime.now()
    def parse(self, response):
        for href in response.xpath('//a/@href'):
            url = response.urljoin(href.extract())
           
            yield scrapy.Request(url, callback=self.parse_dir_contents)
            
    def parse_dir_contents(self,response):
                
        
        for lnk in response.xpath('//div[@class="prod-data"]'):
            if lnk.xpath('@data-newprodid'):
                if lnk.xpath('@data-newprodid').extract() not in self.linkss:
                     self.linkss.append(lnk.xpath('@data-newprodid').extract())
                     items = AllforyouSgItem()
                     items['title'] = lnk.xpath('@data-name').extract()
                     items['price'] = lnk.xpath('@data-price').extract()
                     items['sku'] = lnk.xpath('@data-newprodid').extract()
                     items['primary_image_url'] = lnk.xpath('@data-imgurl').extract()
                     items['currency'] = 'SGD'
                     items['outOfStock'] = lnk.xpath('@data-outofstock').extract()
                     items['oldprice'] = lnk.xpath('@data-oldprice').extract()
                     items['description'] = lnk.xpath('@data-dessc').extract()
                     items['crawltime'] =self.now.strftime("%Y-%m-%d %H:%M:%S")
                     yield items
  
                    

        