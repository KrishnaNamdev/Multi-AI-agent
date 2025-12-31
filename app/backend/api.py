from fastapi import FastAPI,HTTPException
from app.model.models import RequestModel
from typing import List
from app.core.ai_agent import get_response_from_ai_agents
from app.common.custome_exception import CustomException
from app.common.logger import get_logger
from app.config.setting import Setting


logger = get_logger(__name__)

app = FastAPI(title="MULTI AI AGENT")

@app.post("/process_request")
def process_request(request: RequestModel):
    try:
        logger.info(f"Received request: {request}")
        if request.model_name not in Setting.ALLOWED_MODEL_NAMES:
            raise CustomException(status_code=400, message=f"Model {request.model_name} is not supported.")
        response =  get_response_from_ai_agents(request.model_name, request.messages, request.allow_search, request.system_prompt)
        logger.info(f"Response generated from model: {request.model_name}")
        return {"response": response}
    except CustomException as ce:
        logger.error(f"CustomException Occurred: {ce.message}")
        raise HTTPException(status_code=ce.status_code, detail=ce.message)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    