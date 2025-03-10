from generation import call,save_json, extract_json
from erdor import run_erdot
from diagram_generate import generate_diagram

input_requirements=f"""
Patients and appointments

    Each patient can have multiple appointments with different doctors.
    Each appointment can have several tests and diagnoses associated with it.
    The patient's medical record needs to be updated with each new visit.

Doctors and specialties

    A doctor can have more than one specialty (e.g. Cardiology and General Practice).
    Doctors can be teachers and supervisors of residents.
    Doctors can work in different hospitals linked to the university.

Students and Medical Residency

    Students need to accompany doctors on consultations, surgeries and on call.
    A resident can be under the supervision of several doctors, depending on their specialty:

    * Each birthplace can have multiple people associated with it, but each person can only be linked to one birthplace.

Translated with DeepL.com (free version)
"""



def pipeline(requirements, json_file="output.json", dot_file="output.dot"):

    print("Calling LLM")
    llm_response = call(input_requirements)
    print("---------\n")
    print(llm_response)
    print("---------\n")
    print("Cleaning response")
    clean_json = extract_json(llm_response)
    print("Saving response")
    save_json(clean_json, json_file)
    print("Calling erdot")
    dot_file_path = run_erdot(json_file, dot_file)
    print("Generating Image")
    generate_diagram(dot_file_path,)
    return dot_file_path



if __name__ == "__main__": 
    dot_file = pipeline(input_requirements, "example_comparation/json/llama8b.json", "example_comparation/json/llama8b.dot")
    
    if dot_file:
        print(f"Pipeline completed successfully. Final output: {dot_file}")
    else:
        print("Pipeline failed.")

