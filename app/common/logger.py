import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s'
    )

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)