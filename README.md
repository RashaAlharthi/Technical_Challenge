# Technical_Challenge
## ETL Process for Scraping News Websites
This project implements an ETL process for scraping news websites, publishing the scraped articles to Kafka, transforming the data format, and loading it into a MySQL database and MinIO.

## Architecture Diagram
![Architecture Diagram.jpeg](https://github.com/RashaAlharthi/Technical_Challenge/blob/4811d5040e0fa15f430cf2a703b9d4d4f8262aab/Architecture%20Diagram.jpeg)

## Project Steps
__1. Web Scraping__

- There are 4 spiders in this project to scrap the following websites:
   * Al Jazeera
   * BBC
   * Reuters
   * Sky News
- The spiders extract relevant information from each article, such as:
   * Title
   * Publication date
   * Content/Summary
   * Link to the article
   * Source
- For now, the scraper doesn't do pagination and crawling for multiple pages, to simplify the testing of the code and output that running many times.

__2. Kafka Integration__
- Implement a Kafka producer to publish each scraped news article as a message to a Kafka topic.
- Use Scrapy's pipeline to send each article to Kafka one at a time.

__3. MinIO Object Storage__
- Store the scraped news articles as JSON objects in a MinIO bucket called "scraped-news".
- Implement error handling and retries to ensure reliable storage of data.

__4. SQL Data Warehouse__
- Create an ETL process that reads the news articles from Kafka, transforms them into the desired format, and loads them into the SQL database.
- Each message that comes from Kafka Consumer will be transformed to the right format to be loaded successfully in the SQL database table called news_tb.

__5. Automation__
- Create a DAG file for Apache Airflow to trigger the web scraping process at regular intervals.
- Ensure that the automation considers fault tolerance and error handling.

  **_Note:_** Currently, the automation cannot run the tasks due to the different operating systems that run Kafka (Airflow in Linux and Kafka in Windows), and the fact that the scrapy pipeline should run Kafka first to publish the messages.

## Next Step:

- Run Airflow and Kafka in Docker containers. This would allow running them on both Linux and Windows.
- Add more transformations for the data, such as converting the publication date to a Unix timestamp, and cleaning the content of any special character.
- Implement pagination and crawling for multiple pages in the scraper.

# Running the ETL Process
To run the ETL process, follow these steps:

1. Install the required dependencies:
  - Python 3.8 or higher
  - Scrapy --> A Python library for web scraping, can be installed using Python pip install scrapy
  - Kafka --> Apache Kafka is a distributed streaming platform. It can be downloaded from its official site: https://kafka.apache.org/downloads
  - MySQL -->  An open-source relational database management system. Download the (mysql-installer-community-8.0.34.0.msi) from their official site https://dev.mysql.com/downloads/installer/
  - MinIO -->  An open-source object storage server. Download the exe file from this link: https://dl.min.io/server/minio/release/windows-amd64/minio.exe

__2. setting up Kafka:__
  - installing pykafka for Python:
  pip install pykafka
  - Start the Kafka cluster:
  
      - __Step 1__: Open command prompt and change the directory to the kafka folder. First start zookeeper using the command given below:
      
      .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
      
      - __Step 2__: Now open another command prompt and change the directory to the Kafka folder. Run Kafka server using the command:
      
      .\bin\windows\kafka-server-start.bat .\config\server.properties
  
  - Creating a Kafka Topic:
  
      - __Step 1__: Open a new command prompt in the location C:\kafka\bin\windows.
      
     - __Step 2__: Run the following command:
      
      kafka-topics.bat --create --topic quickstart-events --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --

__3. Run the Scrapy Spider:__
    scrapy startproject news_scraper

__4. Run the following command:__
    scrapy crawl SPIDER_NAME

__5. Create a database & table for MySQL__

__7. Create a Bucket for Minio__

__8. Start the connection with MySQL & Minio, then run the Kafka consumer__
__9. Verify that the data is being loaded into the MySQL database and MinIO:__
  - Open the MySQL database and query the news_tb table.
  - Open the MinIO bucket called scraped-news and view the JSON files.

