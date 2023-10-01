import scrapy
from ..items import NewsScraperItem

class Bbc(scrapy.Spider):

    name = "bbc"
    start_urls = ["https://www.bbc.com/news/world"]

    def parse(self, response):
        items = NewsScraperItem()

        # Extract the news articles from the response
        articles = response.css("li.lx-stream__post-container")

        for article in articles:

            title = article.css("article header div h3 span::text").extract()

            # Extract the publication date of the article
            publication_date = article.css("article div div time span.qa-post-auto-meta::text").extract()

            # Extract the content of the article
            content = article.css("article div div p::text").extract()


            # Extract the source of the article 
            link = article.css("article header div h3 a.qa-heading-link.lx-stream-post__header-link::attr(href)").extract()

            link_replace = ["no link found"]
            items["title"] = title
            items["publication_date"] = publication_date
            items["content"] = content
            items["link"] = link or link_replace
            items["source"] = ['BBC']

            yield items
