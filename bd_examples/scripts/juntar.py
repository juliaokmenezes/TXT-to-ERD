import os

def merge_text_files(input_folder, output_file):
    # Verifica se a pasta de entrada existe
    if not os.path.exists(input_folder):
        print(f"Pasta '{input_folder}' não encontrada.")
        return

    # Lista todos os arquivos .txt na pasta em ordem
    text_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.txt')])

    if not text_files:
        print("Nenhum arquivo .txt encontrado na pasta.")
        return

    # Abre o arquivo de saída
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file_name in text_files:
            file_path = os.path.join(input_folder, file_name)
            outfile.write(f"{file_name} :\n")
            with open(file_path, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
            outfile.write("\n" + "-" * 30 + "\n")

    print(f"{len(text_files)} arquivos mesclados em '{output_file}'.")

# Exemplo de uso:
merge_text_files('/home/julia/TXT-to-ERD/bd_examples/txt_examples', 'arquivo_unificado.txt')