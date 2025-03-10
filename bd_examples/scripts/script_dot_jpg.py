import os
import subprocess

pasta = './bd_examples/dot_results'

for arquivo in os.listdir(pasta):
    if os.path.isfile(os.path.join(pasta, arquivo)):
        print(f'Executando comando para: {arquivo}')
        subprocess.run(['dot', arquivo ,'-Tpng','-o', f'{arquivo}.png'], cwd=pasta)
        print(f'Comando executado para: {arquivo}')