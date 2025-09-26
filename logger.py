import logging
import os

from datetime import datetime

LOG_FILE = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

LOG_FILE_PATH = logs_path


logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s]%(lineno)d %(name)s %(levelname)s - %(message)s')


if __name__ == "__main__":
    try:
        logging.info("Starting the logging process.")
        result = 10 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        logging.error("An error occurred", exc_info=True)
        raise CustomException(e)