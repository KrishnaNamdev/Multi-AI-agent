import streamlit as st
import requests

from app.common.logger import get_logger
from app.common.custome_exception import CustomException
from app.config.setting import settings

logger = get_logger(__name__)

st.set_page_config(
    page_title="My Streamlit App",
    layout="centered"
    )

st.title("Welcome to My Streamlit App")

system_prompt = st.text_area("Define your AI system prompt", height=150)
selected_model = st.selectbox("Select AI Model", settings.ALLOWED_MODEL_NAMES)

allow_search = st.checkbox("Enable Web Search", value=False)

user_query = st.text_area("Enter your query here", height=100)

API_URL = "http://127.0.0.1:9999/process_request"

if st.button("Submit") and user_query.strip():
    request_payload = {
        "system_prompt": system_prompt,
        "model_name": selected_model,
        "allow_search": allow_search,
        "messages": [user_query]
    }
    
    try:
        response = requests.post(API_URL, json=request_payload)
        logger.info("Request sent to backend API.")
        if response.status_code == 200:
            agent_response = response.json().get("response", "")

            logger.info("Response received successfully from backend API.")
            st.subheader("AI Response:")
            st.markdown(agent_response.replace("\n", "<br>"), unsafe_allow_html=True)
        else:
            logger.error(f"Error from backend API: {response.status_code} - {response.text}")
            st.error(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        logger.error(f"Exception occurred while calling backend API: {str(e)}")
        st.error(str(CustomException(message="Failed to connect to backend API.")))
