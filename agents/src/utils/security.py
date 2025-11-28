def validate_pdf(file):
    if not file.name.endswith(".pdf"):
        raise ValueError("Arquivo inválido! Apenas PDFs são permitidos.")
    if file.size > 10 * 1024 * 1024:
        raise ValueError("PDF muito grande! Máximo permitido: 10 MB.")

def sanitize(text):
    dangerous = ["system:", "assistant:", "ignore previous", "jailbreak"]
    for d in dangerous:
        text = text.replace(d, "")
    return text
