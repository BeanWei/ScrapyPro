# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from jobs import settings


class JobsPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(settings.MONGO_HOST, int(settings.MONGO_PORT))
        self.db = self.conn[settings.MONGO_DB]

    def process_item(self, item, spider):
        self.db.jobs.save({
            "url": item["url"],
            "pubdate": item["pubdate"],
            "company": item["company"],
            "longitude": item["longitude"],
            "latitude": item["latitude"],
            "city": item["city"],
            "jobtitle": item["jobtitle"],
            "workyear": item["workyear"],
            "salary": item["salary"],    
            "demand": item["demand"]
        })
