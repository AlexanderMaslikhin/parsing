# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class JobsPipeline:
    def __init__(self):
        client = MongoClient("37.140.199.115", 27017)
        self.mdb = client.jobs

    def process_item(self, item, spider):
        collection = self.mdb[spider.name]
        collection.insert_one(item)
        return item
