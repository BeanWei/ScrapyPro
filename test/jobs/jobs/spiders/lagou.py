import scrapy
from scrapy import FormRequest, Request
import json
import math

from jobs.items import JobsItem

class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/']

    url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        "Referer": "https://www.lagou.com/jobs/list_python?px=new&city=%E5%85%A8%E5%9B%BD"
    }

    def start_requests(self):
        post_data = {
            "first": True,
            "pn": 1,
            "kd": "python"
        }
        yield FormRequest(url=self.url, formdata=post_data, callback=self.parse_totalPn)

    def parse_totalPn(self, response):
        res = json.loads(response.body)
        total_page = math.ceil(int(res.get('content').get('positionResult').get("totalCount")) / int(res.get('content').get("pageSize")))
        for pn in range(1, int(total_page)+1):
            if pn == 1:
                post_data = {
                    "first": True,
                    "pn": 1,
                    "kd": "python"
                }  
            else:
                post_data = {
                    "first": False,
                    "pn": pn,
                    "kd": "python"
                } 
            yield FormRequest(url=self.url, formdata=post_data, callback=self.parse_totalUrl)
            
    def parse_totalUrl(self, response):
        item = JobsItem()
        res = json.loads(response.body)
        if (res.get("success")):
            if res.get('content').get('positionResult').get('resultSize') != 0:
                results = res.get('content').get('positionResult').get('result')
                for result in results:
                    item['url'] = "https://www.lagou.com/jobs/{}.html".format(result.positionId)
                    item['pubdate'] = result['createTime']
                    item['company'] = result['companyFullName']
                    item['longitude'] = result['longitude']
                    item['latitude'] = result['latitude']
                    item['city'] = result['city']
                    item['jobtitle'] = result['positionName']
                    item['workyear'] = result['workYear']
                    item['salary'] = result['salary']
                    yield Request(url=item['url'], meta={'item_1': item}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = response.meta['item_1']
        result = ("".join(response.xpath('//dd[@class="job_bt"]//text()').extract())).split("任职要求")[1]
        item['demand'] = re.sub('[\d+\r\n\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+','',result)
        yield item
            
