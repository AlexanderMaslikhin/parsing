import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from jobs.items import JobsSJItem

class SuperjobRuSpider(scrapy.Spider):
    name = "superjob_ru"
    allowed_domains = ["superjob.ru"]
    # start_urls = ["https://www.superjob.ru/vakansii/sistemnyj-administrator.html?geo%5Bt%5D%5B0%5D=4"]
    start_urls = ["https://www.superjob.ru/vacancy/search/?keywords=Python&geo%5Bt%5D%5B0%5D=4"]

    def parse(self, response: HtmlResponse):
        next_page = response.css("a.f-test-button-dalshe::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        #vac_links = response.xpath("//a[@class='serp-item__title']/@href").getall()
        vac_links = response.css("a._2_Rn8::attr(href)").getall()
        for link in vac_links:
            yield response.follow(link, callback=self.parse_vac_links)
        # //a[@class='serp-item__title']
        print(f'**************{response.url}')
        pass

    def parse_vac_links(self, response: HtmlResponse):
        loader = ItemLoader(item=JobsSJItem(), response=response)
        loader.xpath('vac_name', "//h1/text()")
        loader.add_value('vac_link', response.url)
        loader.add_css('vac_salary', 'span._4Gt5t._3Kq5N span::text')
        yield loader.load_item()

    pass
