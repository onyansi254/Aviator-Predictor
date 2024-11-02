import requests
import os
from dotenv import load_dotenv
from utils.logger import get_logger

load_dotenv()
logger = get_logger(__name__)

def collect_data():
    api_key = os.getenv("API_KEY")
    if not api_key:
        logger.error("API_KEY not found in .env")
        return None

    url = f"https://api.example.com/aviator?key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logger.info("Data collected successfully.")
        return data
    except requests.RequestException as e:
        logger.error(f"Error collecting data: {e}")
        return None
 
