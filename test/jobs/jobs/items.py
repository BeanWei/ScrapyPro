# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsItem(scrapy.Item):
    url = scrapy.Field()        #招聘链接
    pubdate = scrapy.Field()    #招聘信息发布时间
    company = scrapy.Field()    #公司名称
    longitude = scrapy.Field()  #公司坐标经度
    latitude = scrapy.Field()   #公司坐标纬度
    city = scrapy.Field()       #就职城市
    jobtitle = scrapy.Field()   #职称
    workyear = scrapy.Field()   #工作年限
    salary = scrapy.Field()     #薪水(区间)
    demand = scrapy.Field()     #工作需求
    