# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Compose, MapCompose, TakeFirst


def clean_price(price):
    return float(price[0].replace(" ", ""))


def clean_photos(photo):
    return photo.split()[0]


class GoodsItem(scrapy.Item):
    good_name = scrapy.Field(input_processor=lambda x: x[0].strip(), output_processor=TakeFirst())
    good_link = scrapy.Field(outpur_processor=TakeFirst())
    good_price = scrapy.Field(input_processor=Compose(clean_price), output_processor=TakeFirst())
    good_photos_urls = scrapy.Field(input_processor=MapCompose(clean_photos))
    good_photos = scrapy.Field()
    _id = scrapy.Field()



