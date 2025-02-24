from model import create_model
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
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


"""

input_requirements=f"""
Consider a website where you can share book reviews. As a user of this site, you can register on the platform, add books to your profile, write and share reviews, rate books, and track your reading progress through the reading status.
"""

def call():
    node_title = "\n\n" + "####################################" + "\n" + (
          "######## Translate Node ############"
    ) + "\n" + "####################################"
    print(node_title)
    
    
    model = create_model("llama3-8b-8192")

    prompt = HumanMessage(f"Translate this requirements into json output: {input_requirements}")
    messages = [
      SystemMessage(system_message),
      prompt
    ]

    final_answer = model.predict_messages(messages).content

    return final_answer


print(call())