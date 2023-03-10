import scrapy
from scrapy.http import HtmlResponse
from goods.items import GoodsItem
from scrapy.loader import ItemLoader

class LeroySpider(scrapy.Spider):
    name = "leroy"
    allowed_domains = ["castorama.ru"]
    site_base = "https://www.castorama.ru"
    start_urls = ["https://www.castorama.ru/catalogsearch/result/?q=%D1%80%D0%B0%D0%BA%D0%BE%D0%B2%D0%B8%D0%BD%D0%B0"]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath('//a[@class="next i-next"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        good_links = response.css("a.product-card__name.ga-product-card-name")
        for link in good_links:
            yield response.follow(link, callback=self.parse_good)
        pass

    def parse_good(self, response: HtmlResponse):
        loader = ItemLoader(item=GoodsItem(), response=response)
        loader.add_xpath("good_name", "//h1/text()")
        price_rub = response.xpath('//span[contains(@id,"product-price")]/span/span/span/text()').get()
        price_kop = response.xpath('//span[contains(@id,"product-price")]/span/span/span/sup/text()').get()
        if price_kop:
            price = price_rub + '.' + price_kop
        else:
            price = price_rub
        loader.add_value("good_price", price)
        image_urls = response.xpath('//img[@class="thumb-slide__img swiper-lazy"]/@data-srcset').getall()
        image_urls = map(lambda x: response.urljoin(x), image_urls)
        loader.add_value("good_photos_urls", image_urls)
        loader.add_value("good_link", response.url)
        yield loader.load_item()

