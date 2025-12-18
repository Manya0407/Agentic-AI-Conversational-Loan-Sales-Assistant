# AI Agentic Loan Sales & Underwriting Prototype

## Overview

This project presents a **working prototype of an Agentic AI–driven personal loan sales and underwriting system** built for the BFSI domain. The solution demonstrates how a digital lender can automate the end-to-end loan journey — from customer interaction to eligibility evaluation and sanction letter generation — using a **master–worker agent architecture**.

The prototype is designed for **hackathon and demo purposes**, using a Streamlit-based frontend and agent-driven backend logic. Dummy data and rule-based decisioning are used to simulate real-world banking workflows in a controlled and explainable manner.

The system follows a **decoupled architecture**, where the frontend is implemented using Streamlit and backend agent services are exposed via FastAPI in the local setup. Communication between the frontend and backend occurs through REST-based HTTP APIs. For demo deployment, agent logic can be co-located within the Streamlit app.

---

## Key Features

* Agentic AI architecture with a **Master Agent** orchestrating multiple **Worker Agents**
* Simulated conversational loan sales flow
* Automated verification and underwriting logic
* Rule-based eligibility checks aligned with BFSI practices
* Automated **PDF sanction letter generation** upon approval
* Graceful fallback handling for missing customer data

---

## Agentic AI Architecture

### Master Agent (Orchestrator)

* Controls the overall workflow and state transitions
* Coordinates interactions between worker agents
* Aggregates decisions and returns final outcomes to the UI

### Worker Agents

* **Sales Agent**: Captures customer loan intent (amount, tenure)
* **Verification Agent**: Fetches KYC and profile data from a dummy CRM dataset
* **Underwriting Agent**:

  * Evaluates credit score eligibility
  * Applies pre-approved limit rules
  * Performs EMI-to-salary validation
* **Sanction Letter Generator**:

  * Generates automated PDF sanction letters for approved loans

This modular agent-based design makes the system extensible, explainable, and suitable for future AI enhancements.

---

## Underwriting Rules Implemented

* Credit score must be **≥ 700**
* If **loan amount ≤ pre-approved limit** → Instant approval
* If **loan amount ≤ 2× pre-approved limit** → Approval only if **EMI ≤ 50% of monthly salary**
* If **loan amount > 2× pre-approved limit** → Rejected

These rules are intentionally kept transparent to reflect responsible lending practices.

---

## Tech Stack

**Frontend**

* Streamlit (Python)

**Backend / Agent Logic**

* FastAPI (local setup)
* Python-based agent orchestration

**Document Generation**

* ReportLab (PDF generation)

**Data Sources (Mocked)**

* CSV-based CRM dataset
* Dummy credit score and income assumptions

---

## Project Structure

```
Loan-Sales-Assistant/
│
├── app.py                     # Streamlit frontend
├── api.py                     # FastAPI backend (local prototype)
├── customers.csv              # Dummy CRM data
├── generate_sanction_pdf.py   # PDF generation logic
├── outputs/                   # Generated sanction letters (gitignored)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How to Run the Prototype (Local Setup)

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the backend (FastAPI)

```bash
uvicorn api:app --reload --port 8000
```

### 3. Start the frontend (Streamlit)

```bash
streamlit run app.py
```

The application will be accessible via the Streamlit interface in your browser.

---

## Demo Scenarios

### ✅ Instant Approval

* Loan amount within pre-approved limit
* Credit score ≥ 700

**Outcome:** Loan approved and sanction letter generated

---

### ⚠️ Conditional Approval

* Loan amount between 1× and 2× pre-approved limit
* EMI validated against salary

**Outcome:** Approval or rejection based on EMI threshold

---

### ❌ Rejection

* Credit score below threshold **OR**
* Loan amount exceeds 2× pre-approved limit

**Outcome:** Loan rejected, no document generated

##

---

## Assumptions & Limitations

* All customer, CRM, and credit bureau data are **synthetic**
* Salary slip upload is simulated and optional
* No real banking, KYC, or payment integrations
* Underwriting is rule-based (no ML models in current scope)

---

## Future Enhancements

* OCR-based salary slip extraction
* LLM-powered conversational chatbot
* Real credit bureau and CRM integrations
* Fraud detection and risk scoring models
* Multi-product loan support

---



This project demonstrates how **Agentic AI principles can be applied to automate and optimize loan sales and underwriting workflows in the BFSI sector**.
