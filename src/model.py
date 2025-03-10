from langchain_groq import ChatGroq
import os

model = "qwen-2.5-32b"
def create_model():
    result = ChatGroq(
        model_name=model,
        groq_api_key=os.getenv("MODEL_API_KEY"),
        temperature=0,
        max_tokens=None,
        request_timeout=35,
        max_retries=3,
    )
    return result