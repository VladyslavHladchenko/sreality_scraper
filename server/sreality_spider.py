# from pathlib import Path
import scrapy
from playwright.async_api import async_playwright
import os


max_results_num_default = 50
env_max_res = os.environ.get('SPIDER_MAX_RESULTS',str(max_results_num_default))
max_results_num = int(env_max_res) if env_max_res.isdecimal() else max_results_num_default

class SrealitySpider(scrapy.Spider):
    name = "sreality"
    start_urls = ["data:,"]  # avoid using the default Scrapy downloader
    
    async def parse(self, response):
        results_count=0
        page_idx = 0
        print(f'Start scraping {max_results_num} items ... ')
        
        async with async_playwright() as pw:
            browser = await pw.chromium.launch()
            
            while results_count < max_results_num:
                page = await browser.new_page()
                page_idx+=1
                await page.goto(f"https://www.sreality.cz/hledani/prodej/byty?strana={page_idx}")
                images = await page.locator('//div[contains(@class, "property")]/preact/div/div/a/img[1]').all()
                names = await page.locator('//span[contains(@class, "name")]').all()
                
                for i,n in zip(images, names):
                    if results_count >= max_results_num:
                        break
                    results_count+=1
                    print(f"yielding from page {page_idx}, result {results_count}/{max_results_num}")
                    
                    img_src = await i.get_attribute('src')
                    name = await n.inner_text()
                    
                    yield {'name':name, 'img_src':img_src}