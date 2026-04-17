# Student Support AI Agent

1. Overview
Python-based AI Agent for student support queries.

2. Files

### `app.py`
Runs the project and handles user input.

### `requirements.txt`
Project dependencies.

### `data/students.py`
Stores student data, FAQs, and escalation keywords.

### `src/agent.py`
Main agent logic and responses.

### `src/intents.py`
Detects user intent.

### `src/utils.py`
Helper functions.

### `src/__init__.py`
Makes `src` a package.

### `tests/test_agent.py`
Project tests.

### `demo/sample_queries.txt`
Sample queries for demo/testing.


Folder Structure

```text
student-support-ai-agent/
│── app.py
│── README.md
│── requirements.txt
│
├── data/
│   └── students.py
│
├── src/
│   ├── __init__.py
│   ├── agent.py
│   ├── intents.py
│   └── utils.py
│
├── tests/
│   └── test_agent.py
│
└── demo/
    └── sample_queries.txt
```
```bash
3. Run
pip install -r requirements.txt
python app.py



