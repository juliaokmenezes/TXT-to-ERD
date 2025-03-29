
from model import create_model
from langchain_core.messages import HumanMessage, SystemMessage
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
            "*name": "varchar(100) NOT NULL",
            "height": "decimal(10,2)NOT NULL",
            "weight": "int()",
            "birthDate": "date()NOT NULL"
        },
        "BirthPlace": {
            "*id_birthplace": "int() NOT NULL",
            "birthCity": "varchar(100)",
            "birthState": "varchar(100)",
            "birthCountry": "varchar(100) NOT NULL",
            "+personName": "varchar(100)"
        }
    },
    "relations": [
        "BirthPlace:personName 1--* Person:name"
    ],
    "rankAdjustments": "",
    "label": ""
}
"""
additional_example_input = """
    Consider a site where it's possible to share book reviews. As a user of this site, you can register on the platform, add books to your profile, write and share reviews, rate books, and track your reading progress through the reading status.
    """

additional_example_output = """
{
  "tables": {
    "User": {
      "*username": "varchar(100) NOT NULL",
      "first_name": "varchar(100)",
      "last_name": "varchar(100)",
      "birth_date": "date()",
      "password": "varchar(100) NOT NULL",
      "profile_picture": "varchar(500)"
    },
    "Book": {
      "*isbn": "varchar(100) NOT NULL",
      "rating": "float() NOT NULL"
    },
    "Review": {
      "*review_id": "bigserial() NOT NULL",
      "+user_username": "varchar(100)",
      "+book_isbn": "varchar(100)",
      "start_date": "date()",
      "end_date": "date()",
      "rate": "integer()",
      "content": "text() NOT NULL"
    },
    "UserBook": {
      "*user_book_id": "bigserial() NOT NULL",
      "+user_username": "varchar(100)",
      "+book_isbn": "varchar(100)",
      "+review_id": "bigint()",
      "status": "varchar(30)"
    }
  },
  "relations": [
    "User:username 1--* Review:user_username",
    "Book:isbn 1--* Review:book_isbn",
    "User:username 1--* UserBook:user_username",
    "Book:isbn 1--* UserBook:book_isbn",
    "Review:review_id 1--* UserBook:review_id"
  ],
  "rankAdjustments": "",
  "label": "book platform"
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
You are a database expert specializing in designing and modeling Entity-Relationship (ER) diagrams. Your task is to analyze a given system description, extract its requirements, and generate a structured ER diagram in JSON format that defines the database model.

### Requirements:

1. **Tables and Attributes**
   - Each table must have a **primary key (marked with `*`)**.
   - Foreign keys must be marked with `+` and reference another table.
   - Attributes should have appropriate data types (`varchar(200)`, `int()`, `date()`, etc.).

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
    - All relations explicitly specify primary and foreign keys in the format Table:PrimaryKey X--X Table:ForeignKey. Even the spaces must be respected
    - Obeserve that in a relation, Table:PrimaryKey there is no space between, you MUST obey this rule DO NOT make the relation like this: [Table: PrimaryKey]
    - rankAdjustments is always an empty list []. "
    - label contains a meaningful title."
    - The output must be in language present on example. If the txt is in english, the output is in english, but if the input is in portuguese, the output MUST be in portuguese
    "Output only the JSON—no additional text, explanations, or comments."
"""


def call(input_requirements):
    model = create_model()
    print(model)

    prompt = f"""
    Here's an additional example to help understand different relationship types:

    #### **Input:**
    {additional_example_input}

    #### **Expected Output:**
    {additional_example_output}

    Now, analyze the following database carefully, extract the requirements, identify tables, keys, and columns and relationships. then generate the ER diagram. Finally, translate it into the required JSON format. 

    You should think about:
      What data needs to be stored in the database? (e.g., users, books, orders)
      What has distinct attributes that need to be recorded?
      What has an independent existence in the system? (e.g., a "User" can exist without an "Order," but an "Order Item" cannot exist without an "Order")
      Is the data type appropriate? (e.g., "name" should be varchar, "price" should be decimal).
      Are there constraints? (NOT NULL, UNIQUE, DEFAULT, etc.).
      How would a relationship between tables work?

    To correctly define relationships, follow this process:

      Identify dependencies: Does an object depend on another to exist? (e.g., a "Comment" depends on a "User" and a "Post")
      Determine cardinality: For each relationship, ask:
      How many elements can be associated with another?
      Can it be zero, one, or many?
      Check if an intermediary table is needed: If there's a "many-to-many" (*--*) relationship, an intermediary entity is required (e.g., "User" and "Book" need "UserBook" to track reading progress).

    To solve this problem, follow these steps:
    1. Identify the main entities from the description
    2. Determine attributes for each entity
    3. Establish primary keys for each entity
    4. Identify relationships between entities 
    5. Determine foreign keys based on relationships
    6. Format everything according to the required JSON structure

    the output json must be inside '''
    Database description: {input_requirements}
    """
    messages = [
      SystemMessage(system_message),
      HumanMessage(prompt)
    ]

    answer_validate = model.invoke(messages).content

    return answer_validate


def save_json(json_content, output_file):
    with open(output_file, 'w') as f:
        json.dump(json_content, f, indent=2)
    return output_file

import re
import json

def extract_json(raw_answer: str):
    try:
        # Try to find JSON within '''json ... ''' or ```json ... ```
        matches = re.findall(r"(?:'''|```)(?:json)?\s*(.*?)\s*(?:'''|```)", raw_answer, re.DOTALL)
        
        if matches:
            raw_answer = matches[-1]  
        else:
            # If no block with '''json''' or ```json```, try to clean manually
            raw_answer = re.sub(r'^(Here.*?:\s*)', '', raw_answer, flags=re.IGNORECASE).strip()
            
        raw_answer = raw_answer.strip() 
        
        return json.loads(raw_answer)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None