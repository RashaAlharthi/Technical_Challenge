# Technical_Challenge
### Project name: ETL Process for Scraping News Websites
This project implements an ETL process for scraping news websites, publishing the scraped articles to Kafka, transforming the data format, and loading it into a MySQL database and MinIO.

### Data Sources
The following news websites are scraped:
- Al Jazeera
- BBC
- Reuters
- Sky News

### Data Extraction
The following information is extracted from each article:
- Title
- Publication date
- Content/Summary
- Source

### Data Transformation
for now, it only transforms the data format to ensure it loads successfully, But I will add more transformations like:

- Convert the publication date to a Unix timestamp.
- clean and strip the content of HTML tags.

### Data Loading
The transformed data is loaded into the following destinations:
- MySQL database: The data is loaded into a table called news_tb.
- MinIO: The data is loaded as a JSON file into a bucket called scraped-news.

## Running the ETL Process
To run the ETL process, follow these steps:

1. Install the required dependencies:
- Python
- Scrapy --> using Python pip install scrapy
- Kafka --> Apache Kafka can be downloaded from its official site: https://kafka.apache.org/downloads
- MySQL --> The (mysql-installer-community-8.0.34.0.msi) from their official site https://dev.mysql.com/downloads/installer/
- MinIO --> Download the exe file from this link: https://dl.min.io/server/minio/release/windows-amd64/minio.exe

2. setting up Kafka:
- installing pykafka for Python:
pip install pykafka
- Start the Kafka cluster:

__Step 1__: Open command prompt and change the directory to the kafka folder. First start zookeeper using the command given below:

.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

__Step 2__: Now open another command prompt and change the directory to the Kafka folder. Run Kafka server using the command:

.\bin\windows\kafka-server-start.bat .\config\server.properties

- Creating a Kafka Topic:

__Step 1__: Open a new command prompt in the location C:\kafka\bin\windows.

__Step 2__: Run the following command:

kafka-topics.bat --create --topic quickstart-events --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --

3. Run the Scrapy Spider:
scrapy startproject news_scraper

4. Run the following command:
scrapy crawl SPIDER_NAME

5. Create a database & table for MySQL

7. Create a Bucket for Minio

8. Start the connection with MySQL & Minio, then run the Kafka consumer
9. Verify that the data is being loaded into the MySQL database and MinIO:
- Open the MySQL database and query the news_tb table.
- Open the MinIO bucket called scraped-news and view the JSON files.

