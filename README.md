🚀 NetSage AI

AI-powered Cisco Packet Tracer network troubleshooting with
deterministic Python rules, Google Gemini AI analysis, and mandatory
human review.

🌐 Live Demo

👉 Open NetSage AI

Live Website: https://netsage-ai-arnav.netlify.app/

📌 About the Project

NetSage AI is an AI-assisted network troubleshooting platform for
Cisco Packet Tracer labs. It combines deterministic Python-based rule
checking with Google Gemini AI to analyze network symptoms, Packet
Tracer observations, and Cisco show command output.

The platform follows a Human-in-the-Loop Responsible AI workflow: AI
generates a diagnosis and recommended fix, but a human reviewer must
Accept, Edit, or Reject the recommendation.

🏗️ Architecture

                         USER
                           │
                           ▼
                  ┌──────────────────┐
                  │   Web Interface  │
                  │    index.html    │
                  └────────┬─────────┘
                           │
                  Symptom + Packet Tracer
                  Notes + Show Commands
                           │
                           ▼
                  ┌──────────────────┐
                  │     FastAPI      │
                  │     Backend      │
                  └────────┬─────────┘
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
     ┌────────────────┐       ┌────────────────┐
     │ Python Rule    │       │  Gemini AI     │
     │ Checker        │       │  Diagnosis     │
     │ 14 Cisco Rules │       │    Engine      │
     └───────┬────────┘       └───────┬────────┘
             │                        │
             └────────────┬───────────┘
                          ▼
              Diagnosis + Evidence + Fix
                          │
                          ▼
                   HUMAN REVIEW
                ┌────────┼────────┐
                ▼        ▼        ▼
             ACCEPT     EDIT    REJECT
                │        │        │
                └────────┼────────┘
                         ▼
                  ┌──────────────┐
                  │  DASHBOARD   │
                  │ Analytics &  │
                  │ Audit Logs   │
                  └──────────────┘

✨ Key Features

🔍 AI Network Diagnosis --- Analyze network symptoms and Cisco
command output.

🧠 Hybrid Diagnosis --- Deterministic Python rules + Gemini AI.

🛡️ Responsible AI --- Human validation is required before final
acceptance.

👨‍💻 Human Review --- Accept, edit, or reject AI-generated
diagnoses.

📊 Dashboard Analytics --- Track total, accepted, edited, and
rejected cases.

📚 30 Troubleshooting Cases --- Preloaded Cisco Packet Tracer
scenarios.

🧾 Evidence-Based Diagnosis --- Results include supporting
evidence and recommended fixes.

📝 AI Audit Logging --- Review decisions and corrections are
recorded.

⚡ FastAPI Backend --- REST API architecture for diagnosis and
case management.

💻 Web-Based UI --- Browser-based interface built with HTML,
CSS, and JavaScript.

📁 Project Structure

NetSage_AI/
│
├── dashboard/
│   └── index.html
│       └── Frontend UI
│          ├── AI Diagnosis
│          ├── Cases
│          ├── Human Review
│          └── Dashboard
│
├── backend/
│   ├── main.py
│   │   └── FastAPI API endpoints
│   │
│   ├── rule_checker.py
│   │   └── Deterministic Cisco regex rules
│   │
│   ├── ai_engine.py
│   │   └── Google Gemini integration
│   │
│   ├── database.py
│   │   └── SQLAlchemy + SQLite setup
│   │
│   ├── models.py
│   │   └── DiagnosticCase database model
│   │
│   └── requirements.txt
│
├── data/
│   ├── cases.csv
│   │   └── 30 Packet Tracer troubleshooting cases
│   │
│   └── responsible_ai_log.csv
│       └── AI audit log with human corrections
│
└── README.md

🔄 How It Works

1. Enter Network Information

The user provides:

Network symptom

Packet Tracer notes

Cisco show command output

2. Python Rule Checker

The backend first checks the input against predefined Cisco
troubleshooting rules.

This provides deterministic and explainable fault detection for known
network conditions.

3. Gemini AI Analysis

Gemini analyzes the network context and provides a contextual diagnosis.

4. Combined Result

NetSage AI presents:

Probable fault

Supporting evidence

Explanation

Recommended corrective action

5. Human Review

The reviewer can:

✅ Accept the diagnosis

✏️ Edit the diagnosis

❌ Reject the diagnosis

6. Dashboard

The review result is recorded and reflected in the dashboard for
monitoring and analysis.

📊 Dashboard

The dashboard provides live diagnostic statistics, including:

Metric        Description

Total Cases   Total diagnostic cases
Accepted      AI diagnoses accepted by the reviewer
Edited        Diagnoses modified by the reviewer
Rejected      Diagnoses rejected by the reviewer

The dashboard also provides a visual case distribution using a donut
chart.

🧪 Dataset

The project contains 30 preloaded Cisco Packet Tracer troubleshooting
cases.

data/cases.csv

AI review and correction information is maintained in:

data/responsible_ai_log.csv

🔌 API Endpoints

Method                  Endpoint                Description

POST                  /api/diagnose         Submit symptom, notes,
and show output for
diagnosis

POST                  /api/review           Submit human review

GET                   /api/stats            Retrieve dashboard
statistics

🛠️ Tech Stack

Component             Technology

Frontend              HTML5, CSS3, Vanilla JavaScript
Backend               Python, FastAPI
Server                Uvicorn
AI Engine             Google Gemini
Rule Engine           Python Regex / Deterministic Rules
Database              SQLite + SQLAlchemy
Charts                Chart.js
Frontend Deployment   Netlify
Backend Deployment    Render / Python-compatible hosting

🚀 Getting Started

Prerequisites

Python 3.10+

pip

Google Gemini API key

Git

1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/NetSage_AI.git
cd NetSage_AI

2. Install Backend Dependencies

cd backend
pip install -r requirements.txt

3. Configure Gemini API

Configure your Gemini API key in the backend.

genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")

⚠️ Security: Never upload your real API key to GitHub. For
production, use environment variables or your hosting platform's
secret/environment-variable settings.

4. Start the Backend

cd backend
python main.py

The API runs on:

http://localhost:8000

5. Open the Frontend

Open:

dashboard/index.html

in your browser.

☁️ Deployment

NetSage AI uses a separated frontend/backend deployment architecture.

Frontend --- Netlify

The live frontend is available at:

🔗 https://netsage-ai-arnav.netlify.app/

Backend

The FastAPI backend can be deployed on:

Render

Railway

Other Python-compatible cloud platforms

After deployment, configure the frontend API URL to point to the
deployed FastAPI backend.

🛡️ Responsible AI

NetSage AI follows a Human-in-the-Loop approach.

AI Diagnosis
     ↓
Human Review
     ↓
Accept / Edit / Reject
     ↓
Audit Log

The AI recommendation is therefore treated as decision support, not
as an automatically authoritative network configuration.

🎯 Project Objective

The goal of NetSage AI is to simplify Cisco Packet Tracer
troubleshooting by combining:

Networking + Deterministic Rules + Generative AI + Human Validation +
Analytics

The project demonstrates how AI can assist students and network
engineers in diagnosing network faults while maintaining transparency,
reviewability, and human oversight.

🌐 Try NetSage AI

🚀 Launch the Live Application

NetSage AI --- Intelligent Network Troubleshooting with Responsible
AI

📄 License

This project is intended for educational and demonstration purposes,
particularly for Cisco Packet Tracer troubleshooting and Responsible AI
experimentation.

Licensed under the MIT License.
