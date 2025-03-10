import os
import subprocess

pasta = './bd_examples/json_examples'

for arquivo in os.listdir(pasta):
    # Verifica se é um arquivo (não uma pasta)
    if os.path.isfile(os.path.join(pasta, arquivo)):
        # Executa o comando erdot para o arquivo
        print(f'Executando comando para: {arquivo}')
        subprocess.run(['erdot', arquivo], cwd=pasta)
        print(f'Comando executado para: {arquivo}')