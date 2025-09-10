from datetime import datetime
from typing import Tuple
import os
import hashlib
import difflib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup


def get_url_hash(url: str) -> str:
    """Generate a unique hash for the URL to use as filename"""
    return hashlib.md5(url.encode()).hexdigest()


def setup_selenium():
    """Set up and return a configured Chrome WebDriver using webdriver-manager"""
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Enable headless mode for GitHub Actions
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_argument('--user-data-dir=/tmp/chrome-user-data')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-plugins')
    chrome_options.add_argument('--disable-images')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--disable-features=VizDisplayCompositor')
    chrome_options.add_argument('--disable-background-timer-throttling')
    chrome_options.add_argument('--disable-backgrounding-occluded-windows')
    chrome_options.add_argument('--disable-renderer-backgrounding')
    chrome_options.add_argument('--disable-features=TranslateUI')
    chrome_options.add_argument('--disable-ipc-flooding-protection')

    # Automatically download and use the correct chromedriver
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)


def fetch_page(url: str) -> str | None:
    print(f"🌐 Fetching page content from {url}")
    driver = None
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            driver = setup_selenium()
            driver.set_page_load_timeout(30)
            driver.get(url)

            # Wait for the page to load with a fixed delay
    append_to_markdown(results)


def main():
    # High-priority URLs that need frequent monitoring (every 6 hours)
    urls = [
        "https://lifeattiktok.com/referral/tiktok/campus/?keywords=Engineer&category=&location=CT_163&project=7459986622530078983%2C7459987887569733896&type=&job_hot_flag=&current=1&limit=10&functionCategory",
        "https://joinbytedance.com/search?job_category_id_list=&location_code_list=CT_163&recruitment_id_list=202%2C301%2C201&subject_id_list=&tag_id_list=&keyword=Engineer&limit=12&offset=0",
        "https://www.linkedin.com/jobs/search-results/?distance=50.0&f_TPR=r21600&geoId=103804675&keywords=software%20engineer&origin=JOBS_HOME_KEYWORD_HISTORY" 
        "https://www.linkedin.com/jobs/search-results/?distance=50.0&f_TPR=r21600&geoId=103804675&keywords=data%20engineer&origin=JOBS_HOME_KEYWORD_HISTORY",
        "https://joinbytedance.com/search?recruitment_id_list=202%2C301%2C201&job_category_id_list=6704215862603155720&subject_id_list=&location_code_list=CT_163&keyword=Data&limit=12&offset=0",
        "https://joinbytedance.com/search?recruitment_id_list=202%2C301%2C201&job_category_id_list=6704215862603155720&subject_id_list=&location_code_list=CT_163&keyword=Engineer&limit=12&offset=0" 
    ]

    process_urls(urls)
    print("\nFrequent scraper completed. Check frequent_changes.md for the log.")


if __name__ == "__main__":
    main()
