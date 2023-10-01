import scrapy
from ..items import NewsScraperItem

class Reuters(scrapy.Spider):

    name = "reuters"
    start_urls = ["https://www.reuters.com"]

    #def parse_article(self, response):

        # Extract the content of the article
        #content = response.css("div.article-body__content__17Yit p::text").extract_first()

        # Set the content of the item
        #items["content"] = content

        #yield content


    def parse(self, response):
        items = NewsScraperItem()

        # Extract the news articles from the response
        articles = response.css("li.story-collection__default__G33_I.story-collection__story__LeZ29.story-collection__with-spacing__1E6N5")
	
        for article in articles:
            # Extract the title of the article
            title = article.css("div div h3 a::text").extract()

            # Extract the publication date of the article
            #publication_date = article.css("time::attr(datetime)").extract()
            publication_date = article.css("div div time::attr(datetime)").extract()

            # Extract the source of the article 
            link = article.css("div a::attr(href)").extract()

            # Go to the link of the article
            #content = yield response.follow(link, callback=self.parse_article)
            
            link_replace = ["no link found"]
            items["title"] = title
            items["publication_date"] = publication_date
            items["content"] = ["no summary available"]
            items["link"] = link or link_replace
            items["source"] = ['Reuters']

            yield items