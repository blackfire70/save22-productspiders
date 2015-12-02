import scrapy


from allforyou_sg.items import AllforyouSgItem
class AllForYouCrawler(scrapy.Spider):
    name = "AFY"
    allowed_domains = ["www.allforyou.sg"]
    start_urls = [
        "https://www.allforyou.sg/"]

    def parse(self, response):
        for href in response.xpath('//a/@href'):
            url = response.urljoin(href.extract())
           
            yield scrapy.Request(url, callback=self.parse_dir_contents)
            
    def parse_dir_contents(self,response):
      
               
        for lnk in response.xpath('//div[@class="prod-data"]'):
             items = AllforyouSgItem()
             items['title'] = lnk.xpath('@data-name').extract()
             items['price'] = lnk.xpath('@data-price').extract()
             items['sku'] = lnk.xpath('@data-newprodid').extract()

             yield items
  
                    

        