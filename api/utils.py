from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def generate_pdf(fir_instance):
    """ Generates a PDF for the FIR """
    pdf_path = os.path.join("media/fir_pdfs", f"{fir_instance.case_id}.pdf")
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 750, f"Case ID: {fir_instance.case_id}")
    c.drawString(100, 730, "Complaint:")
    c.drawString(100, 710, fir_instance.original_text[:500])  # Limiting length
    c.drawString(100, 690, "Generated FIR:")
    c.drawString(100, 670, fir_instance.fir_text[:500])
    c.save()

    return pdf_path
