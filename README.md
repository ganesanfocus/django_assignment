# Agentic AI Research Assistant

## Project Description

This project demonstrates an Agentic AI Research Assistant built using **Django**, **LangGraph**, **CrewAI**, and **Microsoft AutoGen**. The system performs automated web research, summarizes the collected information, and generates a professional report in PDF or DOCX format.

---

## Technologies Used

- Python
- Django
- LangGraph
- CrewAI
- Microsoft AutoGen
- LangChain
- OpenAI / Gemini
- ReportLab
- python-docx

---

## AI Architecture

### CrewAI

CrewAI is used to define each agent's:

- Role
- Goal
- Backstory
- Responsibilities

Example:

- Research Agent
- Summarizer Agent
- Document Creator Agent

---

### Microsoft AutoGen

AutoGen is responsible for:

- Agent-to-Agent communication
- LLM interactions
- Tool calling
- Conversation management

Registered tools include:

- web_search()
- generate_document()

---

### LangGraph

LangGraph orchestrates the complete workflow using a graph architecture.

Workflow includes:

- Nodes
- Edges
- Conditional Routing
- State Management

---

## Workflow

```
                User Query
                     │
                     ▼
             LangGraph Workflow
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
 Research Agent             Search Tool
 (CrewAI + AutoGen)     (Web Search API)
        │
        ▼
 Summarizer Agent
 (CrewAI + AutoGen)
        │
        ▼
 Routing Node
 (Conditional Edge)
        │
        ▼
 Document Creator
 (CrewAI + AutoGen)
        │
        ▼
 PDF / DOCX Generator
```

---

## Agent Details

### Research Agent

Responsibilities

- Search the web
- Collect reliable information
- Pass raw content to Summarizer

Technologies

- CrewAI
- AutoGen
- Web Search Tool

---

### Summarizer Agent

Responsibilities

- Read collected information
- Remove duplicate content
- Generate concise summary

Technologies

- CrewAI
- AutoGen

---

### Document Creator Agent

Responsibilities

- Receive summarized content
- Detect requested output format
- Generate PDF or DOCX

Technologies

- CrewAI
- AutoGen
- ReportLab
- python-docx

---

## Features

- Multi-Agent AI Workflow
- CrewAI Role-Based Agents
- AutoGen Agent Communication
- LangGraph State Management
- Conditional Edge Routing
- Web Search Tool Integration
- Automatic Report Generation
- PDF Export
- DOCX Export

---

## Project Creation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

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

### Run Server

```bash
python manage.py runserver
```

---

## Project Structure

```
djangoagenticai/
│
├── research/
│   ├── agents/
│   │   ├── researcher.py
│   │   ├── summarizer.py
│   │   ├── doc_creator.py
│   │   └── config.py
│   │
│   ├── workflow/
│   │   └── graph.py
│   │
│   ├── tools/
│   │   ├── search_tool.py
│   │   └── doc_generator.py
│   │
│   ├── services/
│   ├── templates/
│   ├── media/
│   ├── views.py
│   └── urls.py
│
├── manage.py
├── .env
├── requirements.txt
└── README.md
```

---

## Output

- Performs automated web research
- Summarizes collected information
- Generates professional reports
- Supports PDF and DOCX export

---