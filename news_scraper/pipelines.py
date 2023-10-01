# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
#import json
from pykafka import KafkaClient 


class NewsScraperPipeline(object):

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        client = KafkaClient(hosts="localhost:9092") #initialize KafkaClient
        self.topic = client.topics['News_ETL']

    def to_producer(self, item):
        producer = self.topic.get_sync_producer()
        producer.produce(bytes(item, 'utf-8'))


    def process_item(self, item, spider):
        item = item['title'][0] + ", "+ item['publication_date'][0] +", "+ item['content'][0] +", "+ item['link'][0] +", "+item['source'][0]
        self.to_producer(item)
        return item