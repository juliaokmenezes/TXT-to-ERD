from langchain_groq import ChatGroq
import os



def create_model(model: str):
    result = ChatGroq(
        model_name=model,
        groq_api_key=os.getenv("MODEL_API_KEY"),
        temperature=0,
        max_tokens=None,
        request_timeout=35,
        max_retries=3,
    )
    return result