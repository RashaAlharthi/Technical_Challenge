import scrapy
from ..items import NewsScraperItem

class Aljazeera(scrapy.Spider):

    name = "aljazeera"
    start_urls = ["https://www.aljazeera.com/news"]

    def parse(self, response):	
	# Iterate over the article links and scrape each article
        #for article_link in news_articles:
        #    yield scrapy.Request(article_link, callback=self.parse_article)

        items = NewsScraperItem()

        # Extract the news articles from the response
        articles = response.css("div.gc__content")

        for article in articles:
            title = article.css("div.gc__header-wrap h3.gc__title a span::text").extract()

            # Extract the publication date of the article
            publication_date = article.css("footer.gc__footer div div div div span:nth-child(2)::text").extract()

            # Extract the content of the article
            content = article.css("div.gc__body-wrap div p::text").extract()

            # Extract the source of the article 
            link = article.css("div.gc__header-wrap h3.gc__title a::attr(href)").extract()

            link_replace = ["no link found"]
            items["title"] = title
            items["publication_date"] = publication_date
            items["content"] = content
            items["link"] = link or link_replace
            items["source"] = ['Aljazeera']

            yield items
