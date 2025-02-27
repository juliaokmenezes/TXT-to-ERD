from generation import call,save_json, extract_json
from erdor import run_erdot
from diagram_generate import generate_diagram

input_requirements=f"""
Consider a website where you can share book reviews. As a user of this site, you can register on the platform, add books to your profile, write and share reviews, rate books, and track your reading progress through the reading status.
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
    input_requirements = """
    Consider a website where you can share book reviews. As a user of this site, you can register on the platform, add books to your profile, write and share reviews, rate books, and track your reading progress through the reading status.
    """
    
    dot_file = pipeline(input_requirements, "output/bookhive3.json", "output/bookhive3.dot")
    
    if dot_file:
        print(f"Pipeline completed successfully. Final output: {dot_file}")
    else:
        print("Pipeline failed.")

