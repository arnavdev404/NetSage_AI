NetSage AI

NetSage AI is a web-based tool for troubleshooting Cisco Packet Tracer
network problems. It takes a network symptom, Packet Tracer notes, and
Cisco show command output and uses a combination of Python-based
checks and Google Gemini to suggest the possible cause and fix.

The main idea is simple: let the system help with the diagnosis, but
keep a human involved before the result is finalized.

Live Website

You can try the working project here:

https://netsage-ai-arnav.netlify.app/

What the Project Does

When a user enters a network problem, NetSage AI:

Takes the network symptom and available Cisco command output.

Checks the information against predefined Python troubleshooting
rules.

Sends the relevant information to Gemini for additional analysis.

Combines the results into a diagnosis with supporting evidence and a
suggested fix.

Allows a human reviewer to accept, edit, or reject the diagnosis.

Stores the review information so it can be viewed through the
dashboard.

This makes the project useful for learning and experimenting with
AI-assisted network troubleshooting without removing human judgment from
the process.

How It Works

User
  |
  v
Network Symptom + Packet Tracer Notes + Show Commands
  |
  v
FastAPI Backend
  |
  +--------------------+
  |                    |
  v                    v
Python Rule Checker   Gemini AI
  |                    |
  +---------+----------+
            |
            v
     Diagnosis + Evidence + Fix
            |
            v
       Human Review
       /     |      \
   Accept   Edit   Reject
       \     |      /
            v
        Dashboard

Main Features

Network fault diagnosis for Cisco Packet Tracer labs

Python-based deterministic checks for common Cisco issues

Gemini AI for additional analysis and explanation

Human review of AI-generated results

Accept, Edit, and Reject workflow

Dashboard showing diagnostic statistics

30 predefined troubleshooting cases

AI review and correction logging

REST API built with FastAPI

Simple browser-based frontend

Project Structure

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

What the important files do

dashboard/index.html
Contains the web interface for diagnosis, cases, review, and dashboard
pages.

backend/main.py
Runs the FastAPI application and provides the API endpoints.

backend/rule_checker.py
Contains the predefined Python rules used to identify known Cisco
troubleshooting conditions.

backend/ai_engine.py
Handles the Gemini AI part of the diagnosis.

backend/database.py and models.py
Set up the SQLite database and diagnostic case model.

data/cases.csv
Contains the 30 Packet Tracer troubleshooting cases used by the project.

data/responsible_ai_log.csv
Keeps track of AI recommendations and human review/correction
information.

Technologies Used

Frontend: HTML, CSS, JavaScript

Backend: Python, FastAPI, Uvicorn

AI: Google Gemini

Database: SQLite, SQLAlchemy

Rule Checking: Python Regular Expressions

Charts: Chart.js

Frontend Hosting: Netlify

Running the Project Locally

Requirements

You will need:

Python 3.10 or newer

pip

A Google Gemini API key

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/NetSage_AI.git
cd NetSage_AI

2. Install the backend packages

cd backend
pip install -r requirements.txt

3. Add your Gemini API key

Configure the API key used by ai_engine.py.

For example:

genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")

For a real deployment, it is better to keep the key in an environment
variable rather than committing it to GitHub.

4. Start the backend

python main.py

The FastAPI server should be available at:

http://localhost:8000

5. Open the frontend

Open:

dashboard/index.html

in your browser.

API Endpoints

Method   Endpoint          Purpose

POST   /api/diagnose   Analyze a network problem
POST   /api/review     Save a human review
GET    /api/stats      Get dashboard statistics
GET    /api/cases      Get troubleshooting cases

Dashboard

The dashboard gives a quick view of the cases handled by the system.

It includes:

Total cases

Accepted diagnoses

Edited diagnoses

Rejected diagnoses

Case distribution chart

The review information is also useful for seeing where the AI diagnosis
needed human correction.

Human Review

One of the important parts of NetSage AI is that the AI result is not
treated as the final answer automatically.

After a diagnosis is generated, a reviewer can:

Accept it if the diagnosis is correct.

Edit it if some part needs to be changed.

Reject it if the diagnosis is not useful or correct.

The review is then recorded in the system.

AI suggests a diagnosis
          ↓
     Human checks it
          ↓
  Accept / Edit / Reject
          ↓
       Saved result

Troubleshooting Cases

The project currently includes 30 Cisco Packet Tracer troubleshooting
scenarios.

These cases are stored in:

data/cases.csv

They can be used to test the diagnosis workflow and demonstrate
different network fault conditions.

Deployment

The frontend is currently deployed on Netlify:

https://netsage-ai-arnav.netlify.app/

The FastAPI backend can be deployed separately using a Python-compatible
hosting service such as Render.

When deploying the project, make sure the frontend is configured to
communicate with the deployed backend URL.

Why We Built It

Troubleshooting a Packet Tracer network can involve checking several
things at once: interfaces, IP addresses, routing, VLANs, configuration
commands, and command output.

NetSage AI was built to make that process easier by putting those inputs
into one place and providing an initial diagnosis.

The project also explores how AI can be used as an assistant rather
than replacing the person making the final decision.

Future Improvements

Some possible improvements are:

Add more Cisco troubleshooting rules

Support additional network devices and command outputs

Improve the diagnostic history

Add authentication for multiple users

Add more detailed evaluation metrics

Improve backend deployment and monitoring

Expand the troubleshooting dataset

License

This project is made for educational and demonstration purposes.

Licensed under the MIT License.
