from langchain_groq import ChatGroq
import os

model = "mixtral-8x7b-32768"
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