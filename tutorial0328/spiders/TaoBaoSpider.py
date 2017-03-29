# -*- coding: utf-8 -*-

from selenium import webdriver
from scrapy import Spider,Selector

class TaoBaoSpider(Spider):
    """
    淘宝Spider，继承自scrapy.Spider
    @name spider名字，可以根据名字启动指定spider
    @allowed_domains 限定spider爬取的域
    @start_urls 开始爬取的域

    @def(self, response) spider通过下载器下载好的内容回调，可以获取网页内容

    启动命令: scrapy crawl taobao_spider
    """

    name = "taobao_spider"
    allowed_domains = ["tmail.com", "taobao.com"]
    start_urls = []
    total_items = 0

    def __init__(self, *args, **kwargs):
        super(TaoBaoSpider, self).__init__(*args, **kwargs)
        self.count = 0
        self.error_count = 0

        # 指定chrome webdriver本地路径
        self.driver = webdriver.Chrome(executable_path="D:/python/chromedriver.exe")
        
        # 淘宝女装主页
        url = 'https://www.taobao.com/markets/nvzhuang/taobaonvzhuang'
        self.start_urls.append(url)

    def __del__(self):
        if self.driver is not None:
            self.driver.quit() # 退出

    #  解析
    def parse(self, response):
        return self._parse_handler(response)

    def _parse_handler(self, response):
        self.logger.info("parse url---:{0}".format(response.url))
        self.driver.get(response.url)
        # Selector allows you to select parts of an XML or HTML text using CSS
        # or XPath expressions and extract data from it.
        selector = Selector(text=self.driver.page_source)
        print(selector.extract())

