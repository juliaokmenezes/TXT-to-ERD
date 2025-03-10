from generation import call,save_json, extract_json
from erdor import run_erdot
from diagram_generate import generate_diagram
import os

def read_requirements(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()



def pipeline(requirements_file, output_folder):
    print(f"Processing {requirements_file}")
    input_requirements = read_requirements(requirements_file)
    
    print("Calling LLM")
    llm_response = call(input_requirements)
    print("---------\n")
    print(llm_response)
    print("---------\n")
    
    print("Cleaning response")
    clean_json = extract_json(llm_response)
    
    base_name = os.path.splitext(os.path.basename(requirements_file))[0]
    json_file = os.path.join(output_folder, f"{base_name}.json")
    dot_file = os.path.join(output_folder, f"{base_name}.dot")
    
    print("Saving response")
    save_json(clean_json, json_file)
    
    print("Calling erdot")
    dot_file_path = run_erdot(json_file, dot_file)
    
    print("Generating Image")
    generate_diagram(dot_file_path)
    
    return dot_file_path



if __name__ == "__main__":
    requirements_folder = "./bd_examples/txt_examples/temp"  
    output_folder = "./output/bd"  

    files = sorted(os.listdir(requirements_folder))  
    
    for file_name in files:
            file_path = os.path.join(requirements_folder, file_name)
            dot_file = pipeline(file_path, output_folder)
            
            if dot_file:
                print(f"Pipeline completed successfully for {file_name}. Final output: {dot_file}")
            else:
                print(f"Pipeline failed for {file_name}.")

