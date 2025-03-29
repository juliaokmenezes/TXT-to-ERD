import os
import subprocess

pasta = '/home/julia/TXT-to-ERD/avaliacao/json-oraculo'

for arquivo in os.listdir(pasta):
    if os.path.isfile(os.path.join(pasta, arquivo)):
        print(f'Executando comando para: {arquivo}')
        subprocess.run(['erdot', arquivo], cwd=pasta)
        print(f'Comando executado para: {arquivo}')