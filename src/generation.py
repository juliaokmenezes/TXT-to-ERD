
from model import create_model
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import json
import re
import os


example_input= f"""
A system for registering people and their birthplaces requires a database that stores information about individuals and their respective places of birth. The system should allow the registration of people and birthplaces, as well as efficiently link individuals to their birthplaces. This system must meet the following requirements:

    * Each birthplace can have multiple people associated with it, but each person can only be linked to one birthplace.

"""
example_output = """
{
    "tables": {
        "Person": {
            "*name": "char()",
            "height": "int()",
            "weight": "int()",
            "birthDate": "date()",
            "+birthPlaceID": "int()"
        },
        "BirthPlace": {
            "*id": "int()",
            "birthCity": "char()",
            "birthState": "char()",
            "birthCountry": "char()"
        }
    },
    "relations": [
        "Person:birthPlaceID *--1 BirthPlace:id"
    ],
    "rankAdjustments": "",
    "label": ""
}
"""

json_fmt = """
{
    "tables": {
        "TableName": {
            "*PrimaryKey": "DataType",
            "+ForeignKey": "DataType",
            "Attribute": "DataType"
        }
    },
    "relations": [
        "TableOne:PrimaryKey 1--* TableTwo:ForeignKey"
    ],
    "rankAdjustments": "...",
    "label": "..."
}
"""


system_message = f"""
You are an expert data engineer responsible for designing and implementing relational databases. Your task is to analyze a given system description and generate a structured JSON output that defines the database schema. 

### Requirements:

1. **Tables and Attributes**
   - Each table must have a **primary key (marked with `*`)**.
   - Foreign keys must be marked with `+` and reference another table.
   - Attributes should have appropriate data types (`char()`, `int()`, `date()`, etc.).

2. **Relationships**
   - Define entity relationships in the format:
     ```
     "TableOne:PrimaryKey 1--* TableTwo:ForeignKey"
     ```
   - The left side represents the referencing table.
   - The right side represents the referenced table.
   - Use proper cardinality indicators:
     - `?` → 0 or 1  
     - `1` → Exactly 1  
     - `*` → 0 or more  
     - `+` → 1 or more  

### Output Format:

Your response **must** strictly follow this JSON structure:

{json_fmt}

### Example:

#### **Input:**
{example_input}

#### **Expected Output:**
{example_output}

 ENSURE THAT: 
    - All relations explicitly specify primary and foreign keys in the format Table:PrimaryKey X--X Table:ForeignKey. 
    - rankAdjustments is always an empty list []. "
    - label contains a meaningful title."
    "Output ONLY the JSON without any additional text."
"""


def call(input_requirements):
    model = create_model("llama3-8b-8192")

    prompt = HumanMessage(f"Translate this requirements into json output: {input_requirements}")
    messages = [
      SystemMessage(system_message),
      prompt
    ]

    answer_validate = model.invoke(messages).content

    return answer_validate


def save_json(json_content, output_file):
    with open(output_file, 'w') as f:
        json.dump(json_content, f, indent=2)
    return output_file

def extract_json(raw_answer: str):
    try:
        matches = re.findall(r'```json\s*(.*?)\s*```', raw_answer, re.DOTALL)
        if matches:
            raw_answer = matches[-1]
        else:
            raw_answer = re.sub(r'^(Here is the JSON output based on the given requirements:\s*)', '', raw_answer, flags=re.IGNORECASE).strip()

        return json.loads(raw_answer)

    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        return None

    






'''prompt_extract = HumanMessage(f"Read the description of the database, and extract requirements, tables, keys and columns. this is the description : {input_requirements}")
    messages_extract = [
      prompt_extract
    ]

    answer_initial = model.predict_messages(messages_extract).content

    prompt_json = HumanMessage(f"Translate this informations into the json output {answer_initial}")
    messages_json = [
      SystemMessage(system_message),
      prompt_json
    ]

    answer_json = model.predict_messages(messages_json).content

    prompt_validate = HumanMessage(f"Validate if json is in correct format regarding rules and descriptions. Give me ONLY the json {answer_json}")
    messages = [
      SystemMessage(system_message),
      prompt_json
    ]

    answer_validate = model.predict_messages(messages).content'''