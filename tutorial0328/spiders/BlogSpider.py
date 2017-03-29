# -*- coding: utf-8 -*-

import scrapy

class BlogSpider(scrapy.Spider):
    """
    解析 https://blog.scrapinghub.com 博客中的数据


    """
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('h2.entry-title'): # 博客列表标题
            yield {'title': title.css('a::text').extract_first()} # 提取a标签中的text的属性
        
        next_page = response.css('div.prev-post>a::attr(href)').extract_first() # 提取下一页链接
        print("{0} 下一个链接".format(next_page))
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse) # 使用递归的方式去解析下一页的内容


