import subprocess
import re

def generate_diagram(dot_file, output_format="png"):

    limpar_chave_extra(dot_file)
    
    output_file = dot_file.replace('.dot', f'.{output_format}')

    cmd = ["dot", f"-T{output_format}", dot_file, "-o", output_file]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error running Graphviz: {result.stderr}")
        return None
    
    return output_file




def limpar_chave_extra(arq):

    with open(arq, "r", encoding="utf-8") as f:
        conteudo = f.read()

    conteudo_limpo = re.sub(r'\n\s*\[\]\s*\n', '\n', conteudo)

    with open(arq, "w", encoding="utf-8") as f:
        f.write(conteudo_limpo)
    



