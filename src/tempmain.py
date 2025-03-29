from erdor import run_erdot
from diagram_generate import generate_diagram
import os

def process_existing_json(json_folder, output_folder):
    try:
        files = sorted(os.listdir(json_folder))  # Lista os arquivos JSON na pasta
        
        for file_name in files:
            if file_name.endswith(".json"):  # Processa apenas arquivos JSON
                file_path = os.path.join(json_folder, file_name)
                
                print(f"Processing {file_name}")
                
                base_name = os.path.splitext(file_name)[0]
                dot_file = os.path.join(output_folder, f"{base_name}.dot")

                print("Calling erdot")
                dot_file_path = run_erdot(file_path, dot_file)

                print("Generating Image")
                generate_diagram(dot_file_path)

                print(f"Pipeline completed successfully for {file_name}. Final output: {dot_file_path}")

    except Exception as e:
        print(f"Error processing JSON files: {e}")

if __name__ == "__main__":
    json_folder = "/home/julia/TXT-to-ERD/avaliacao/json-oraculo"  # Pasta onde os JSON já existem
    output_folder = "/home/julia/TXT-to-ERD/avaliacao/oraculo"  # Pasta para saída dos arquivos .dot e imagens

    process_existing_json(json_folder, output_folder)
