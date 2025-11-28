import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_address, body, txt_file, docx_file):
    from_address = "seuemail@example.com"
    subject = "Resumo PDF"
    
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Adicionar anexos
    with open(txt_file, "rb") as file:
        attachment = MIMEText(file.read(), 'plain')
        attachment.add_header('Content-Disposition', 'attachment', filename=txt_file)
        msg.attach(attachment)

    with open(docx_file, "rb") as file:
        attachment = MIMEText(file.read(), 'plain')
        attachment.add_header('Content-Disposition', 'attachment', filename=docx_file)
        msg.attach(attachment)

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(from_address, "senha_do_email")
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        return "✅ Email enviado com sucesso."
    except Exception as e:
        return f"❌ Erro ao enviar email: {e}"
