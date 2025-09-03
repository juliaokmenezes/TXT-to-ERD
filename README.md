# TXT-to-ERD

## About

**TXT-to-ERD** is a Python-based tool designed to convert `.txt` files containing relational database requirements into **ERD** (Entity–Relationship Diagrams).  
This project was developed to support readers of the associated research paper, making it easier to **visualize and validate database models** directly from textual descriptions.

---

## Repository Contents

This repository includes:

- `arquivo_unificado.txt`: text file with relational model specifications to be converted into an ERD.
- `src/`: main source code of the tool, including parsing and diagram generation modules.
- `bd_examples/`: sample `.txt` files to test and illustrate the tool’s functionality.
- `output/`: directory where generated diagrams (PNG, SVG, PDF, etc.) are stored.
- `historico/` and `avaliacao/`: historical data and evaluation-related files.
- `.gitignore`: files and folders ignored by Git.
- `.gitmodules`: submodules configuration, if external dependencies are used.
- `requirements.txt`: Python dependencies required to run the project.

---

## Requirements

To run the tool, you will need:

- **Python 3.7+**
- Dependencies listed in `requirements.txt` (e.g., `pygraphviz`, `pydot`, `graphviz`, depending on implementation inside `src/`).

Make sure you also have **Graphviz** installed and available in your system’s PATH.  
[Download Graphviz](https://graphviz.org/download/)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/juliaokmenezes/TXT-to-ERD.git
   cd TXT-to-ERD
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Command-line execution

```bash
python src/main.py --input path/to/file.txt --output output/diagram.png
```

**Arguments:**

- `--input`: path to the `.txt` file containing database requirements.
- `--output`: path and name of the generated ERD file (e.g., `ERD.png`, `ERD.svg`).

### Example

Generate a diagram from the provided example:

```bash
python src/main.py --input bd_examples/example1.txt --output output/example1_erd.png
```

The diagram will be saved under the `output/` directory.

---

## Example Input File Format

The `.txt` file should follow the defined structure, for example:

```text
ENTITY: Customer (id_customer, name, email)
ENTITY: Order (id_order, date, total_value)
RELATIONSHIP: Customer 1:N Order
```

- `ENTITY`: defines a table with attributes.
- `RELATIONSHIP`: defines the relationship type between entities (e.g., 1:1, 1:N, N:M).

> **Note:** Adapt the syntax according to the detailed rules presented in the paper.  
Cardinalities, constraints, or foreign keys can also be expressed.

---

## Examples

In the `bd_examples/` directory you will find sample `.txt` inputs such as:

- `example1.txt`: a simple model with two entities and a 1:N relationship.
- `example2.txt`: a more complex model with M:N relationships and composite attributes.

Run them with the tool to explore different outputs.

---
## License

*(If applicable)*

```text
This project is licensed under the MIT License. See the LICENSE file for details.
```

---
