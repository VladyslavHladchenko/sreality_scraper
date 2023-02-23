set -e

cd scraper
scrapy crawl sreality -O props.json
python json_to_db.py
streamlit run serve_page.py
