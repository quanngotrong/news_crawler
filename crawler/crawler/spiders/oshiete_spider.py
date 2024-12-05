from pathlib import Path

import scrapy


class OshieteSpider(scrapy.Spider):
    name = "oshiete"

    def start_requests(self):
        urls = [
            "https://oshiete.goo.ne.jp/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = f"test.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
