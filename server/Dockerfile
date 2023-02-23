FROM python:latest
WORKDIR /code
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN playwright install
RUN playwright install-deps
RUN scrapy startproject scraper

COPY sreality_spider.py /code/scraper/scraper/spiders/
COPY json_to_db.py /code/scraper/
COPY serve_page.py /code/scraper/
COPY start.sh start.sh

CMD ["bash", "-u", "start.sh"]