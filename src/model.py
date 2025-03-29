from langchain_groq import ChatGroq
import os



# Configuração do modelo
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
