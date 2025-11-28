from fpdf import FPDF

def export_chat_to_pdf(history):
    if not history:
        return None

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for i, (question, answer) in enumerate(history, 1):
        pdf.multi_cell(0, 10, f"Q{i}: {question}")
        pdf.multi_cell(0, 10, f"A{i}: {answer}")
        pdf.ln(5)

    if not os.path.exists('outputs'):
        os.makedirs('outputs')

    pdf_path = f"outputs/chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf.output(pdf_path)

    return pdf_path
