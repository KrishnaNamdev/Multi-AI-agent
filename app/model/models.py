from pydantic import BaseModel

class RequestModel(BaseModel):
    model_name: str
    system_prompt: str 
    allow_search: bool
    messages : list[str]
