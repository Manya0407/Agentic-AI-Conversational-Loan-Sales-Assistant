# api.py
from fastapi import FastAPI
from pydantic import BaseModel
import csv, os
from fastapi.responses import FileResponse

app = FastAPI()
DATA_FILE = 'customers.csv'
OUTPUT_DIR = 'outputs'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load customers from CSV
customers = {}
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, newline='') as f:
        reader = csv.DictReader(f)
        for r in reader:
            # store by lowercase name
            customers[r['name'].strip()] = r

@app.get('/crm')
def get_crm(name: str):
    name = name.strip()
    profile = customers.get(name)

    if profile:
        return {
            "name": profile.get('name'),
            "phone": profile.get('phone'),
            "preapproved_limit": profile.get('preapproved_limit'),
            "credit_score": profile.get('credit_score'),
            "monthly_salary": profile.get('monthly_salary')
        }

    # fallback dummy response
    return {
        "name": name,
        "phone": "0000000000",
        "preapproved_limit": "150000",
        "credit_score": "750",
        "monthly_salary": "30000"
    }

class UnderwriteRequest(BaseModel):
    name: str
    loan_amount: int
    tenure: int

@app.post('/underwrite')
def underwrite(req: UnderwriteRequest):
    name = req.name.strip()
    profile = customers.get(name)

    # load profile or fallback
    if profile:
        credit_score = int(profile.get('credit_score', 750))
        pre_limit = int(profile.get('preapproved_limit', 150000))
        salary = int(profile.get('monthly_salary', 30000))
    else:
        credit_score = 750
        pre_limit = 150000
        salary = 30000

    decision = 'REJECT'
    reason = ''
    pdf_path = ''

    # underwriting rules
    if credit_score < 700:
        decision = 'REJECT'
        reason = 'Low credit score'
    elif req.loan_amount <= pre_limit:
        decision = 'APPROVE'
        reason = 'Within pre-approved limit'
    elif req.loan_amount <= 2 * pre_limit:
        expected_emi = req.loan_amount / req.tenure  # simplified
        if expected_emi <= 0.5 * salary:
            decision = 'APPROVE'
            reason = 'EMI within 50% of salary'
        else:
            decision = 'REJECT'
            reason = 'EMI exceeds 50% of salary'
    else:
        decision = 'REJECT'
        reason = 'Above 2× pre-approved limit'

    # generate sanction PDF only if approved
    if decision == 'APPROVE':
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.pdfgen import canvas
            fname = os.path.join(OUTPUT_DIR, f"sanction_{name.replace(' ', '_')}.pdf")
            c = canvas.Canvas(fname, pagesize=A4)
            c.setFont('Helvetica', 12)
            c.drawString(50, 800, f"Sanction Letter - {name}")
            c.drawString(50, 780, f"Approved Amount: INR {req.loan_amount}")
            c.drawString(50, 760, f"Tenure (months): {req.tenure}")
            c.drawString(50, 740, "This is a prototype sanction letter.")
            c.save()
            pdf_path = fname
        except:
            # fallback text file
            fname = os.path.join(OUTPUT_DIR, f"sanction_{name.replace(' ', '_')}.txt")
            with open(fname, "w") as f:
                f.write(f"Sanction Letter - {name}\nApproved: {req.loan_amount}\nTenure: {req.tenure}\n")
            pdf_path = fname

    return {
        "decision": decision,
        "reason": reason,
        "sanction_pdf_path": pdf_path
    }
