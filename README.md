# 🌐 NetSage AI

> **AI-assisted Cisco Packet Tracer troubleshooting with deterministic rules, Gemini analysis, and human review.**

NetSage AI is a web-based network troubleshooting assistant built for **Cisco Packet Tracer labs**.

Instead of manually going through configuration output, IP addresses, interfaces, routing information, and other command results, you can give NetSage AI the problem description and available `show` command output. The system combines **Python-based troubleshooting rules** with **Google Gemini** to identify possible causes and suggest a practical fix.

The important part is that **AI does not get the final say**.

A human reviewer can accept, edit, or reject the generated diagnosis before it becomes a recorded result.

---

## 🚀 Live Demo

### Try NetSage AI

** [Open the Live Website](https://netsage-ai-arnav.netlify.app/)**

The frontend is currently hosted on **Netlify**.

---

##  Why NetSage AI?

Troubleshooting a Cisco Packet Tracer network is often less about knowing one command and more about connecting several pieces of information.

For example:

* Is an interface administratively down?
* Is the IP address incorrect?
* Is a VLAN missing?
* Is a routing entry unavailable?
* Is a subnet configured incorrectly?
* Is the command output pointing toward another issue?

NetSage AI brings these inputs together and gives the user an initial diagnosis instead of making them manually inspect everything from scratch.

The goal is not to replace the network engineer.

**The goal is to give the engineer a useful starting point.**

---

#  How It Works

```text
             👤 User
                │
                ▼
      Network Symptom
      Packet Tracer Notes
      Cisco Show Commands
                │
                ▼
        ┌─────────────────┐
        │   FastAPI API   │
        └────────┬────────┘
                 │
        ┌────────┴────────┐
        ▼                 ▼
┌───────────────┐  ┌───────────────┐
│ Python Rules  │  │  Gemini AI    │
│ Deterministic │  │ AI Analysis   │
└───────┬───────┘  └───────┬───────┘
        │                  │
        └────────┬─────────┘
                 ▼
       Diagnosis + Evidence
              + Fix
                 │
                 ▼
          Human Review
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
    ✅ Accept   Edit   ❌ Reject
       │         │         │
       └─────────┼─────────┘
                 ▼
             Dashboard
```

---

# ✨ Features

###  AI-Assisted Diagnosis

Uses Google Gemini to analyze the provided network information and generate a possible diagnosis with explanation and suggested remediation.

###  Deterministic Python Rules

Known Cisco troubleshooting conditions are checked using predefined Python logic and regular expressions.

This gives the system a predictable layer instead of depending entirely on an AI response.

### 👨‍💻 Human-in-the-Loop Review

Every generated diagnosis can be reviewed by a person.

**Accept →** Diagnosis is correct
**Edit →** Diagnosis needs correction
**Reject →** Diagnosis is not useful or correct

### 📊 Dashboard

The dashboard provides a quick overview of diagnostic activity, including review outcomes and case distribution.

###  30 Troubleshooting Cases

The project includes **30 predefined Cisco Packet Tracer troubleshooting scenarios** that can be used to test and demonstrate the system.

### REST API

The backend exposes REST API endpoints through FastAPI, making the diagnosis and review workflow easy to integrate with the frontend.

---

# 🏗️ Project Structure

```text
NetSage_AI/
│
├── dashboard/
│   └── index.html
│
├── backend/
│   ├── main.py
│   ├── rule_checker.py
│   ├── ai_engine.py
│   ├── database.py
│   ├── models.py
│   └── requirements.txt
│
├── data/
│   ├── cases.csv
│   └── responsible_ai_log.csv
│
└── README.md
```

---

# 📁 Important Files

| File                          | Purpose                                                    |
| ----------------------------- | ---------------------------------------------------------- |
| `dashboard/index.html`        | Web interface for diagnosis, cases, reviews, and dashboard |
| `backend/main.py`             | FastAPI application and API routes                         |
| `backend/rule_checker.py`     | Deterministic troubleshooting rules                        |
| `backend/ai_engine.py`        | Gemini AI integration                                      |
| `backend/database.py`         | SQLite database configuration                              |
| `backend/models.py`           | Database models                                            |
| `data/cases.csv`              | 30 predefined troubleshooting scenarios                    |
| `data/responsible_ai_log.csv` | Stores AI recommendations and human review information     |

---

# 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

### Backend

* Python 3.10+
* FastAPI
* Uvicorn

### AI

* Google Gemini

### Database

* SQLite
* SQLAlchemy

### Rule Engine

* Python
* Regular Expressions

### Deployment

* Netlify for the frontend
* Python-compatible hosting for the backend

---

# ⚙️ Running Locally

## Requirements

Before running NetSage AI locally, make sure you have:

* **Python 3.10 or newer**
* **pip**
* **Google Gemini API key**

---

##  Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/NetSage_AI.git
cd NetSage_AI
```

---

##  Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

---

##  Configure Gemini

Set your Gemini API key in the AI configuration.

For example:

```python
genai.configure(
    api_key="YOUR_GEMINI_API_KEY_HERE"
)
```

### Important

For real deployments, **do not commit your API key to GitHub**.

Use environment variables or another secure secret-management approach instead.

---

## Start the Backend

From the `backend` directory:

```bash
python main.py
```

The FastAPI server should then be available at:

```text
http://localhost:8000
```

---

## Open the Frontend

Open:

```text
dashboard/index.html
```

in your browser and make sure the frontend is configured to use the correct backend URL.

---

# API Endpoints

| Method | Endpoint        | Description                               |
| ------ | --------------- | ----------------------------------------- |
| `POST` | `/api/diagnose` | Analyze a network troubleshooting problem |
| `POST` | `/api/review`   | Save a human review                       |
| `GET`  | `/api/stats`    | Get dashboard statistics                  |
| `GET`  | `/api/cases`    | Get predefined troubleshooting cases      |

---

# 📊 Dashboard

The dashboard provides a simple overview of how the system is being used.

It includes information such as:

```text
Total Cases
    │
    ├── ✅ Accepted
    ├── ✏️ Edited
    └── ❌ Rejected
```

The case distribution chart makes it easier to see how often the AI-generated diagnosis was accepted, modified, or rejected.

The review information also gives insight into where the AI needed human correction.

---

# 👨‍💻 Human Review Workflow

One of the core ideas behind NetSage AI is **human oversight**.

The system follows this workflow:

```text
AI generates diagnosis
        ↓
Human reviews result
        ↓
 ┌──────┼───────┐
 ↓      ↓       ↓
Accept  Edit   Reject
 └──────┼───────┘
        ↓
   Save the result
```

This means an AI-generated response is treated as a **recommendation**, not an unquestionable answer.

That makes the project especially useful for experimenting with **responsible AI in technical troubleshooting**.

---

# Troubleshooting Dataset

NetSage AI currently contains **30 Cisco Packet Tracer troubleshooting scenarios**.

The cases are stored in:

```text
data/cases.csv
```

These scenarios are used to test the complete diagnosis → review → logging workflow.

They also provide a consistent set of examples for demonstrating how the rule engine and AI analysis work together.

---

# Deployment

The frontend is currently deployed on Netlify:

**https://netsage-ai-arnav.netlify.app/**

The FastAPI backend can be deployed separately on a Python-compatible platform such as **Render**.

When deploying the application, update the frontend configuration so that API requests point to the deployed backend rather than:

```text
http://localhost:8000
```

Also make sure your Gemini API key is stored securely on the backend.

---

#  Future Improvements

NetSage AI is still an evolving project.

Some improvements planned for future versions include:

* More Cisco troubleshooting rules
* Support for additional network devices
* More `show` command types
* Better diagnostic history
* User authentication
* More detailed evaluation metrics
* Backend monitoring
* Larger troubleshooting datasets
* Improved AI evaluation and correction tracking

---

#  Project Goal

NetSage AI was created to explore a simple question:

> **Can AI make network troubleshooting easier without taking the human out of the process?**

The project combines traditional rule-based logic with generative AI, while keeping a human reviewer in the loop.

That combination makes NetSage AI more than just a chatbot for networking.

It is an experiment in building a **practical, explainable, and human-reviewed AI troubleshooting workflow**.

---

#  License

This project is created for **educational and demonstration purposes**.

Licensed under the **MIT License**.

---

## ⭐ Support the Project

If you find NetSage AI interesting, consider giving the repository a ⭐ on GitHub.

```text
Built with Python + FastAPI + Gemini + a lot of network troubleshooting.
```

**NetSage AI — Diagnose smarter. Review carefully. Troubleshoot better.**
