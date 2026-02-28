<img width="1382" height="324" alt="Screenshot 2026-02-28 125203" src="https://github.com/user-attachments/assets/c4dcb4db-998a-4ca7-bf88-c5c28f925a4a" />

<img width="1855" height="654" alt="Screenshot 2026-02-28 125147" src="https://github.com/user-attachments/assets/bec06df8-7841-4a80-81e5-36edc7bf0459" />

# HR Policy Decision Service

A simple, rule-based backend service designed for an Employee Self Service (ESS) system. This API accepts an employee's HR-related question and returns a structured decision based on predefined policies.

Built with **Python** and **FastAPI**, this solution focuses on clear code structure, logical separation of concerns, and graceful error handling.

## Project Structure

* `main.py`: The FastAPI application, defining the API endpoints and input/output validation.
* `decision_logic.py`: The core business logic containing the deterministic, rule-based engine. It operates independently of the web framework.
* `requirements.txt`: The required Python dependencies.

## Setup Instructions

**1. Install dependencies:**
Make sure you have Python installed, then install the required packages:
```bash
pip install -r requirements.txt


