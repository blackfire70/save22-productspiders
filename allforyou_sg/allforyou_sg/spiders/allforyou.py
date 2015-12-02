import scrapy


from allforyou_sg.Items import AllforyouSgItem

class AllForYouCrawler(Scrapy.Spider):
    name = "AFY"
    allowed_domains = ["www.allforyou.sg"]
    start_urls = [
        "https://allforyou.sg/"]

    def parse(self, response):
        for href in response.xpath('ul[@class="treemenu"//a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)
            
    def parse_dir_contents(self,response):

        pass
