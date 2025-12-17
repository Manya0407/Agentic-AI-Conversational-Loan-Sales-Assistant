import streamlit as st
import requests
import base64
import os

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Agentic Loan Assistant", layout="wide")

st.title("Hi! I’m Tata Capital’s AI assistant. How can I help you today?")

st.markdown("""
This prototype demonstrates:
- CRM retrieval  
- Automated underwriting  
- Dynamic workflow  
- Sanction letter generation  
""")

# --- INPUT SECTION ---
st.header("1. Customer & Loan Inputs")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Customer name")
    loan_amount = st.number_input("Requested Loan Amount (INR)", min_value=10000, step=5000)

with col2:
    tenure = st.number_input("Tenure (months)", min_value=6, max_value=60, step=6)


# --- CRM FETCH ---
st.header("2. Fetch CRM Profile")
if st.button("Fetch CRM Profile"):
    try:
        res = requests.get(f"{BACKEND_URL}/crm", params={"name": name})
        crm = res.json()
        st.success("CRM retrieved successfully.")
        st.json(crm)
    except Exception as e:
        st.error("Backend error. Is API running?")
        st.exception(e)


# --- UNDERWRITING ---
st.header("3. Run Underwriting Worker")
uw_result = None

if st.button("Run Underwriting Worker"):
    try:
        payload = {"name": name, "loan_amount": loan_amount, "tenure": tenure}
        res = requests.post(f"{BACKEND_URL}/underwrite", json=payload)
        uw_result = res.json()
        st.json(uw_result)

        # Show sanction file if exists
        if uw_result.get("decision") == "APPROVE":
            pdf_path = uw_result.get("sanction_pdf_path", "")
            if pdf_path and os.path.exists(pdf_path):
                st.success(f"Loan approved — sanction letter generated at: `{pdf_path}`")

                # Display PDF download button
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="Download Sanction PDF",
                        data=f,
                        file_name=os.path.basename(pdf_path),
                        mime="application/pdf"
                    )
        else:
            st.warning(f"Loan rejected: {uw_result.get('reason')}")

    except Exception as e:
        st.error("Error calling underwriting API.")
        st.exception(e)


# --- CONDITIONAL: SALARY SLIP UPLOAD ---
if uw_result and "EMI exceeds" in uw_result.get("reason", ""):
    st.header("4. Upload Salary Slip (Only If Required)")

    uploaded = st.file_uploader("Upload salary slip", type=["pdf", "png", "jpg", "jpeg"])

    if uploaded:
        st.success("Salary slip received (demo placeholder).")
        st.info("OCR processing + GPT underwriting will be used here in future updates.")
