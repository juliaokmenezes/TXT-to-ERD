from model import create_model
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import json
import re
import os



example = """
1. Cadastro de Imóveis
1.1. Cada imóvel deve estar obrigatoriamente vinculado a um único proprietário.
1.2. Um proprietário pode possuir vários imóveis.
Intermediação de Corretores
2.1. Cada imóvel deve ser administrado por um único corretor.
2.2. Um corretor pode administrar vários imóveis.
Locação de Imóveis
3.1. Um imóvel pode ser alugado para no máximo um inquilino por vez.
3.2. Um inquilino pode alugar um ou mais imóveis simultaneamente.
Gestão de Propriedade e Representação
4.1. Um proprietário deve delegar a um único corretor a gestão (de alugueis) de seus imóveis (todos os imóveis de um determinado proprietário são administrados pelo mesmo corretor).
4.2. Um corretor pode representar vários proprietários na gestão de seus imóveis.

"""


def clean_text(input_folder, output_folder):
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
            Verifique se nos requisitos para geração de um diagrama entidade-relacionamento abaixo exitem pontos de melhora como frases confusas e/ou ambiguas.
            
            {content}

            Você pode tomar com um bom exemplo de especificação de requisitos o seguinte exemplo, nesse exemplo voce deve tomar como inspiração a forma como as frases foram escritas, e não o conteúdo que o texto explicita:
            {example}

            por favor, corrija o texto enviado de acordo com o pedido acima. Não invente novos requisitos, apenas corrija os que estão detalhados no texto original
            """

        system_message = SystemMessage(content="Este é um assistente para correção e adeuqação de requisitos para diagramas entidade relacionamento")
        human_message = HumanMessage(content=prompt)

        messages = [system_message, human_message]

        translated_text = llm.invoke(messages).content

        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(translated_text)

        print(f"Arquivo '{file_name}' traduzido e salvo em '{output_folder}'.")

# Exemplo de uso:
clean_text('/home/julia/TXT-to-ERD/bd_examples/txt_pt_examples','/home/julia/TXT-to-ERD/bd_examples/txt_new_examples' )
