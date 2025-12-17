# generate_sanction_pdf.py
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
os.makedirs('outputs', exist_ok=True)
fname = os.path.join('outputs','sanction_demo.pdf')
c = canvas.Canvas(fname, pagesize=A4)
c.setFont('Helvetica', 12)
c.drawString(50, 800, 'Sanction Letter - Demo Customer')
c.drawString(50, 780, 'Approved Amount: INR 150000')
c.drawString(50, 760, 'Tenure: 24 months')
c.save()
print('Wrote', fname)
