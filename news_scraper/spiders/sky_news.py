import scrapy
from ..items import NewsScraperItem

class Skynews(scrapy.Spider):

    name = "skynews"
    start_urls = ["https://feeds.skynews.com/feeds/rss/world.xml"]

    def parse(self, response):
        items = NewsScraperItem()

        # Extract the news articles from the response hub-card__body__2nu6n
        articles = response.css("item")

        for article in articles:
            # Extract the title of the article //ul[@id='carousel-container']/li[1]/div/div/div/a
            title = article.css("title::text").extract()

            # Extract the publication date of the article
            publication_date = article.css("pubDate::text").extract()

            # Extract the content of the article
            content = article.css("description::text").extract()

            # Extract the source of the article 
            link = article.css("link::text").extract()

            items["title"] = title
            items["publication_date"] = publication_date
            items["content"] = content
            items["link"] = link
            items["source"] = ['SkyNews']

            yield items