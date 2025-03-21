from langchain_groq import ChatGroq
import os
MODEL_API_KEY="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"

model = "llama3-70b-8192"
def create_model():
    result = ChatGroq(
        model_name=model,
        groq_api_key=MODEL_API_KEY,
        temperature=0,
        max_tokens=None,
        request_timeout=35,
        max_retries=3,
    )
    return result