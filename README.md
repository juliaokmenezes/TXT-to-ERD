# TXT-to-ERD

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)
## About
**TXT-to-ERD** is a Python-based tool that automatically converts `.txt` files with **relational database requirements** into **Entity–Relationship Diagrams (ERDs)**.  
It was created as part of the research project:

> *Database Modeling Automation from Natural Language Requirements*  
> Júlia O. K. Menezes, Claudio E. C. Campelo – Federal University of Campina Grande (UFCG)
---

## Features

- Parse natural language requirements from plain text files.
- Extract **entities, attributes, and relationships** automatically.
- Generate ER diagrams using **ERDot** + **Graphviz**.
- Support for **cardinalities** (1:1, 1:N, N:M).
- Works with multiple input examples and outputs visual diagrams (`.png`, `.svg`, `.pdf`).
- Includes a dataset of examples for testing and evaluation.

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
- 
## License

```text
This project is licensed under the MIT License. See the LICENSE file for details.
```

---
