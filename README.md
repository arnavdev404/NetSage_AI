# NetSage AI

> AI-powered Cisco Packet Tracer lab fault diagnosis with deterministic Python rules, Google Gemini AI analysis, and mandatory human review.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Gemini](https://img.shields.io/badge/Google%20Gemini-AI%20Engine-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Architecture

```
         USER
          │
    ┌─────────────┐
    │  index.html  │   ← Frontend (browser)
    └──────┬──────┘
           │
    ┌─────────────┐
    │   FastAPI    │   ← Backend (Python API)
    └──────┬──────┘
        ╱       ╲
┌────────────┐ ┌─────────────┐
│   Python   │ │  Gemini AI  │
│   Rule     │ │  Diagnosis  │
│   Checker  │ │             │
└─────┬──────┘ └──────┬──────┘
      └───────┬───────┘
              │
    Diagnosis + Evidence + Fix
              │
    👨‍💻 HUMAN REVIEW
    Accept / Edit / Reject
              │
         DASHBOARD
```

---

## Project Structure

```
NetSage_AI/
├── dashboard/              ← Frontend
│   └── index.html          ← Single-page UI (Diagnosis, Cases, Review, Dashboard)
│
├── backend/                ← Backend (Python FastAPI)
│   ├── main.py             ← API endpoints
│   ├── rule_checker.py     ← Deterministic Cisco regex rule checks
│   ├── ai_engine.py        ← Google Gemini AI integration
│   ├── database.py         ← SQLAlchemy + SQLite setup
│   ├── models.py           ← DiagnosticCase DB model
│   └── requirements.txt    ← Python dependencies
│
├── data/                   ← Reference datasets
│   ├── cases.csv           ← 30 Packet Tracer troubleshooting cases
│   └── responsible_ai_log.csv ← AI audit log with human corrections
│
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- A Google Gemini API key

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/NetSage_AI.git
cd NetSage_AI
```

### 2. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Configure API Key

Open `backend/ai_engine.py` and replace the API key with your own Gemini key:

```python
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")
```

### 4. Start the Backend Server

```bash
cd backend
python main.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

> **Keep this terminal running.**

### 5. Open the Frontend

Open `dashboard/index.html` in any web browser. That's it!

- On **Windows**: Double-click `dashboard\index.html`
- On **Mac/Linux**: `open dashboard/index.html` or `xdg-open dashboard/index.html`

---

## Usage

1. **AI Diagnosis** — Enter a network symptom, Packet Tracer notes, and show-command output. Click **Diagnose**. The system runs Python rules first, then Gemini AI, and returns a combined result.

2. **Human Review** — Select a pending case, review the AI diagnosis, and mark it as **Accept**, **Edit**, or **Reject**. All decisions are logged.

3. **Dashboard** — View live statistics: total cases, accepted, edited, rejected, with a donut chart.

4. **Cases** — Browse all 30 pre-loaded Packet Tracer troubleshooting scenarios.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/diagnose` | Submit symptom + notes + show output for diagnosis |
| `POST` | `/api/review` | Submit human review (accept / edit / reject) |
| `GET` | `/api/stats` | Get dashboard statistics |
| `GET` | `/api/cases` | Get all diagnostic cases |

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Backend | Python, FastAPI, Uvicorn |
| AI Engine | Google Gemini 3.5 Flash |
| Rule Checker | Python regex (14 Cisco rules) |
| Database | SQLite via SQLAlchemy |
| Charts | Chart.js |

---

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for step-by-step instructions on deploying the backend on **Render** and the frontend on **Netlify** (both free).

---

## License

This project is for educational purposes — Cisco Packet Tracer lab troubleshooting with Responsible AI oversight.
