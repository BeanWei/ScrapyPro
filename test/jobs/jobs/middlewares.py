# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

import telnetlib
import random
# from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

# from jobs.haipproxy.client.py_cli import ProxyFetcher
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware


class JobsSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JobsDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# class RotateUserAgentMiddleware(UserAgentMiddleware):
#     user_agent_list = [
#         'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31',
#         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like'
#         'Gecko) Chrome/24.0.1312.60 Safari/537.17',
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chr'
#         'ome/24.0.1309.0 Safari/537.17',
#         'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; '
#         '.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
#         'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
#         'Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
#         'Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
#         'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1',
#         'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:15.0) Gecko/20120910144328 Firefox/15.0.2',
#         'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
#         'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
#         'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.13; ) Gecko/20101203',
#         'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
#         'Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50',
#         'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52',
#         'Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285',
#         'Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.7pre) Gecko/20070815'
#         ' Firefox/2.0.0.6 Navigator/9.0b3',
#         'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
#     ]

#     def __init__(self, user_agent = ''):
#         self.user_agent = user_agent

#     def _user_agent(self, spider):
#         if hasattr(spider, 'user_agent'):
#             return spider.user_agent
#         elif self.user_agent:
#             return self.user_agent

#         return random.choice(self.user_agent_list)

#     def process_request(self, request, spider):
#         ua = self._user_agent(spider)
#         if ua:
#             request.headers.setdefault('User-Agent', ua)


class IPProxyMiddleware(HttpProxyMiddleware):
    pool_list = [
        '103.74.246.124:65301',
        '103.87.139.26:8080',
        '110.36.234.214:8080',
        '112.66.244.98:8641',
        '113.121.245.134:8641',
        '114.215.95.188:8627',
        '114.235.3.76:8060',
        '117.242.145.103:8080',
        '119.28.37.58:80',
        '120.199.64.163:8622',
        '121.8.98.197:8939',
        '123.119.188.220:8060',
        '123.12.70.139:8204',
        '138.68.231.41:8860',
        '144.217.204.254:8840',
        '168.0.216.92:8977',
        '168.128.29.75:8464',
        '180.162.228.155:8060',
        '180.173.43.116:8716',
        '183.23.74.53:8537',
        '186.46.85.194:53005',
        '190.104.245.39:8305',
        '190.9.59.76:8298',
        '191.102.97.99:8155',
        '191.252.92.248:9010',
        '194.182.74.203:8873',
        '200.72.187.75:8108',
        '201.245.172.157:80',
        '201.245.201.18:9030',
        '202.100.83.139:9044',
        '207.148.74.8:8452',
        '212.237.61.15:9023',
        '217.61.98.52:8773',
        '217.61.98.52:8981',
        '218.91.156.188:808',
        '219.141.168.249:8908',
        '222.139.8.45:8060',
        '222.16.83.18:8915',
        '222.186.45.58:57624',
        '222.85.22.159:61234',
        '222.93.12.14:8118',
        '223.146.254.91:808',
        '27.13.214.178:61202',
        '27.152.113.187:8118',
        '27.204.85.159:61234',
        '27.37.121.195:8272',
        '27.37.121.195:8607',
        '27.37.121.195:8766',
        '27.37.121.195:8818',
        '34.240.231.232:3128',
        '35.227.26.224:3128',
        '36.26.211.172:61202',
        '36.59.87.19:61202',
        '36.6.12.97:61234',
        '36.66.37.185:8080',
        '39.76.86.92:61202',
        '42.237.159.179:8060',
        '42.54.88.57:34946',
        '43.247.68.211:3128',
        '43.250.81.140:8080',
        '45.226.50.4:8285',
        '45.226.50.4:8457',
        '45.226.50.4:9047',
        '45.32.195.95:8498',
        '45.32.201.221:8968',
        '45.76.56.140:8121',
        '45.77.88.109:8080',
        '47.89.10.103:80',
        '49.84.196.235:9074',
        '49.86.24.214:8060',
        '49.89.87.221:8888',
        '54.223.94.193:3128',
        '54.255.135.61:8742',
        '54.38.51.181:3128',
        '58.19.63.64:8724',
        '59.33.41.87:61234',
        '60.188.25.19:8832',
        '60.194.11.179:8951',
        '61.135.217.7:80',
        '61.136.163.245:8168',
        '61.136.163.246:8707',
        '62.231.245.5:8626',
        '66.70.147.195:8464',
        '82.200.205.49:8957',
        '83.212.106.250:8159',
        '83.212.106.250:8293',
        '83.212.106.250:8307',
        '89.29.26.77:3128',
        '91.239.55.129:8080',
        '93.190.142.240:8873',
        '94.253.127.217:8883',
        '94.65.214.133:8799'
    ]

    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        # fetcher = ProxyFetcher('zhihu', strategy='greedy')
        # thisIP = random.choice(fetcher.get_proxies())
        thisIP = random.choice(self.pool_list)
        ip, port = thisIP.split(':')
        try:
            telnetlib.Telnet(ip, port, timeout=2)
            print(ip)
            request.meta['proxy'] = "http://" + thisIP
        except:
            pass
