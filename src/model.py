from langchain_openai import ChatOpenAI
import os



# Configuração do modelo
def create_model():
    model = ChatOpenAI(
        model_name="gpt-4o",  
        openai_api_key=OPENAI_API_KEY,
        temperature=0,
        max_tokens=1000  
    )
    return model
