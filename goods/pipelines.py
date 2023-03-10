# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import os
from pymongo import MongoClient


class GoodsPipeline:

    def __init__(self):
        client = MongoClient("37.140.199.115", 27017)
        self.mdb = client.goods

    def process_item(self, item, spider):
        collection = self.mdb[spider.name]
        collection.insert_one(item)
        return item


class GoodPhotoPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if item['good_photos_urls']:
            try:
                adapter = ItemAdapter(item)
                for media in adapter['good_photos_urls']:
                    yield scrapy.Request(media)
            except Exception as e:
                print(e)

    def item_completed(self, results, item, info):
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        im_name = request.url.split('/')[-1]
        im_dir = item['good_name']
        return os.path.join(im_dir, im_name)

