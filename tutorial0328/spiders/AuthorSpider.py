# -*- coding: utf-8 -*-

from scrapy import Spider

class AuthorSpider(Spider):
    """
    提取博客中博主信息
    """
    name = "author_spider"

    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):

        for href in response.css("span.author + a::attr(href)"):
            yield response.follow(href, self._parse_author)
        
        # 下一页
        for href in response.css(".next>a::attr(href)"):
            yield response.follow(href, self.parse)

    def _parse_author(self, response):
        
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            "name": extract_with_css(".author-details h3.author-title::text"),
            "birthday": extract_with_css("span.author-born-date::text")
        }