# Agentic AI Research Assistant

## Project Description

This project demonstrates an Agentic AI workflow using Django and LangGraph. The application performs web research, summarizes the collected information using AI agents, and generates a final report in PDF or DOCX format.

---

## Technologies Used

- Python
- Django
- LangGraph
- LangChain
- OpenAI / Gemini API
- python-docx
- ReportLab

---

## Features

- Research Agent – Searches the web for the given topic.
- Summarizer Agent – Summarizes the research content.
- Routing Node – Uses conditional edges to control the workflow.
- Document Node – Generates the final report in PDF or DOCX format.

---

## Workflow

```
User Query
     │
     ▼
Research Agent
     │
     ▼
Summarizer Agent
     │
     ▼
Conditional Routing
     │
     ▼
Document Generator
     │
     ▼
PDF / DOCX Report
```

---

## Project Creation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

### Create Django Project

```bash
django-admin startproject djangoagenticai
```

### Create Django App

```bash
python manage.py startapp research
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Server

```bash
python manage.py runserver
```

Open the browser and visit:

```
http://127.0.0.1:8000/
```

---

## Project Structure

```
djangoagenticai/
│
├── research/
│   ├── agents/
│   ├── services/
│   ├── tools/
│   ├── workflow/
│   ├── templates/
│   ├── media/
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── manage.py
├── db.sqlite3
├── .env
└── README.md
```

---

## Output

- Accepts a research topic from the user.
- Searches the web using the Research Agent.
- Summarizes the collected information.
- Generates a research report in **PDF** or **DOCX** format.

---

## Author

**Ganesan J**