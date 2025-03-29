import os
import subprocess

# Diretório de entrada (onde estão os arquivos .dot)
pasta_entrada = '/home/julia/TXT-to-ERD/avaliacao/json-oraculo/dot'

# Diretório de saída (onde os arquivos .png serão salvos)
pasta_saida = '/home/julia/TXT-to-ERD/avaliacao/oraculo'

# Criar a pasta de saída caso não exista
os.makedirs(pasta_saida, exist_ok=True)

# Percorre os arquivos na pasta de entrada
for arquivo in os.listdir(pasta_entrada):
    caminho_arquivo = os.path.join(pasta_entrada, arquivo)
    
    if os.path.isfile(caminho_arquivo):  # Verifica se é um arquivo
        nome_saida = os.path.splitext(arquivo)[0] + ".png"  # Substitui extensão por .png
        caminho_saida = os.path.join(pasta_saida, nome_saida)  # Caminho final do output
        
        print(f'Executando comando para: {arquivo}')
        subprocess.run(['dot', caminho_arquivo, '-Tpng', '-o', caminho_saida])
        print(f'Arquivo gerado: {caminho_saida}')
