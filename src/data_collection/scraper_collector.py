import requests
from bs4 import BeautifulSoup
from utils.logger import get_logger

logger = get_logger(__name__)

def scrape_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the desired data (update selector as needed)
        crash_value = float(soup.select_one('.crash-value').text)
        logger.info("Scraped data successfully.")
        return crash_value
    except Exception as e:
        logger.error(f"Error scraping data: {e}")
        return None

