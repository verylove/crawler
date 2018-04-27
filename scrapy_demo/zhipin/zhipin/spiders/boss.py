# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from zhipin.items import ZhipinItem

class BossSpider(CrawlSpider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/h_100010000/?query=python&page=1']

    rules = (
        Rule(LinkExtractor(r".+query=python&page=\d"),follow=True),
        Rule(LinkExtractor(r".+job_detail/\d+\.html"),callback="parse_job",follow=False)
    )

    def parse_job(self, response):
        name = response.xpath("//h1[@class='name']/text()").get()
        salary = response.xpath("//h1[@class='name']/span/text()").get().strip()
        job_info = response.xpath("//div[@class='job-primary']/div[@class='info-primary']/p//text()").getall()
        city = job_info[0]
        work_years = job_info[1]
        education = job_info[2]
        company = response.xpath("//div[@class='info-company']/h3/a/text()").get()
        item = ZhipinItem(name=name,salary=salary,city=city,work_years=work_years,education=education,company=company)
        print('='*30)
        print(item)
        print('='*30)
        yield item