import os
import subprocess

pasta = './bd_examples/json_examples'

for arquivo in os.listdir(pasta):
    if os.path.isfile(os.path.join(pasta, arquivo)):
        print(f'Executando comando para: {arquivo}')
        subprocess.run(['erdot', arquivo], cwd=pasta)
        print(f'Comando executado para: {arquivo}')