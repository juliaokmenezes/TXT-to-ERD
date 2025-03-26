from langchain_openai import ChatOpenAI
import os


OPENAI_API_KEY="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"


# Configuração do modelo
def create_model():
    model = ChatOpenAI(
        model_name="gpt-4o",  
        openai_api_key=OPENAI_API_KEY,
        temperature=0,
        max_tokens=1000  
    )
    return model
