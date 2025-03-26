from model import create_model
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import json
import re
import os




def translate_folder_to_portuguese(input_folder, output_folder):
    if not os.path.exists(input_folder):
        print(f"Pasta de entrada '{input_folder}' não encontrada.")
        return

    os.makedirs(output_folder, exist_ok=True)

    text_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.txt')])

    if not text_files:
        print("Nenhum arquivo .txt encontrado na pasta.")
        return

    llm = create_model()

    for file_name in text_files:
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()

        prompt = f"""
            Traduza o seguinte texto para o português, mantendo a sintaxe e a coerência. Não altere a estrutura ou o significado do conteúdo, e preserve o máximo possível da integridade original:
            {content}
            """

        system_message = SystemMessage(content="Este é um assistente para traduzir textos para o português.")
        human_message = HumanMessage(content=prompt)

        messages = [system_message, human_message]

        translated_text = llm.invoke(messages).content

        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(translated_text)

        print(f"Arquivo '{file_name}' traduzido e salvo em '{output_folder}'.")

# Exemplo de uso:
translate_folder_to_portuguese('/home/julia/TXT-to-ERD/bd_examples/txt_examples', '/home/julia/TXT-to-ERD/bd_examples/txt_pt_examples')
