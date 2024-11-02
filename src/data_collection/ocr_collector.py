import cv2
import pytesseract
from utils.logger import get_logger

logger = get_logger(__name__)

def extract_text_from_image(image_path):
    try:
        img = cv2.imread(image_path)
        text = pytesseract.image_to_string(img)
        crash_value = float(text.strip())  # Assuming the crash value is the extracted text
        logger.info("Text extracted from image successfully.")
        return crash_value
    except Exception as e:
        logger.error(f"Error extracting text from image: {e}")
        return None

