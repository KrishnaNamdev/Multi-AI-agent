import subprocess
import threading
import time
from app.common.logger import get_logger
from app.common.custome_exception import CustomException
from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)

def start_backend_service():
    try:
        logger.info("Starting backend service...")
        process = subprocess.run(["uvicorn", "app.backend.api:app", "--host", "127.0.0.1", "--port", "9999"],check=True)
        logger.info("Backend service started.")
        return process
    except Exception as e:
        logger.error(f"Failed to start backend service: {str(e)}")
        raise CustomException(message="Failed to start backend service.") from e
    

def start_frontend_service():
    try:
        logger.info("Starting frontend service...")
        process = subprocess.run(["streamlit", "run", "app/frontend/ui.py"],check=True)
        logger.info("Frontend service started.")
        return process
    except Exception as e:
        logger.error(f"Failed to start frontend service: {str(e)}")
        raise CustomException(message="Failed to start frontend service.") from e

if __name__ == "__main__":
    try:

        threading.Thread(target=start_backend_service).start()
        time.sleep(2)  # Wait for backend to initialize

        start_frontend_service()

    except CustomException as e:
        logger.error(f"Exception in main: {str(e)}")