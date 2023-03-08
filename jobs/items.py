# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Compose, TakeFirst
from jobs.salary_process import salary_hh_process, salary_sj_process


class JobsHHItem(scrapy.Item):
    vac_name = scrapy.Field(output_processor=TakeFirst())
    vac_link = scrapy.Field(output_processor=TakeFirst())
    vac_salary = scrapy.Field(input_processor=Compose(salary_hh_process), output_processor=TakeFirst())
    _id = scrapy.Field()


class JobsSJItem(scrapy.Item):
    vac_name = scrapy.Field(output_processor=TakeFirst())
    vac_link = scrapy.Field(output_processor=TakeFirst())
    vac_salary = scrapy.Field(input_processor=Compose(salary_sj_process), output_processor=TakeFirst())
    _id = scrapy.Field()
