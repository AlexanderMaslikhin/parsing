from scrapy.http import HtmlResponse
import scrapy
from scrapy.loader import ItemLoader
from jobs.items import JobsHHItem


class HhRuSpider(scrapy.Spider):
    name = "hh_ru"
    allowed_domains = ["hh.ru"]
    start_urls = ["https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%BD%D1%8B%D0%B9+%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%BE%D1%80&excluded_text=&area=1&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=1&items_on_page=20"]
    # start_urls = ["https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%BD%D1%8B%D0%B9+%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%BE%D1%80&excluded_text=&area=1&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20"]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        vac_links = response.xpath("//a[@class='serp-item__title']/@href").getall()
        for link in vac_links:
            yield response.follow(link, callback=self.parse_vac_links)
        # //a[@class='serp-item__title']
        print(f'**************{response.url}')
        pass

    def parse_vac_links(self, response: HtmlResponse):

        loader = ItemLoader(item=JobsHHItem(), response=response)
        loader.add_css('vac_name', "h1.bloko-header-section-1::text")
        loader.add_value('vac_link', response.url.split("?")[0])
        loader.add_xpath('vac_salary', '//div[@data-qa="vacancy-salary"]//text()')
        yield loader.load_item()

        pass