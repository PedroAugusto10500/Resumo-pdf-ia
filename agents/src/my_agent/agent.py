import os
from datetime import datetime
from PyPDF2 import PdfReader
from docx import Document
from dotenv import load_dotenv
import openai
from pdf2image import convert_from_path
import pytesseract
import logging
from .history_manager import HistoryManager

# Carrega chave da OpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configura logging
if not os.path.exists("logs"):
    os.makedirs("logs")
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Agent:
    def __init__(self, model="gpt-4.1"):
        self.model = model
        self.system_prompt = "Você é um assistente útil, direto e claro."
        self.history_manager = HistoryManager()

    # ---------- PDF ----------
    def read_pdf(self, filepath: str) -> str | None:
        try:
            reader = PdfReader(filepath)
            pages = [p.extract_text() or "" for p in reader.pages]
            text = "\n".join(pages).strip()

            # Se PDF só tiver imagens, usa OCR
            if not text:
                images = convert_from_path(filepath)
                ocr_text = ""
                for img in images:
                    ocr_text += pytesseract.image_to_string(img, lang='por+eng') + "\n"
                text = ocr_text.strip()

            if not text:
                logging.warning(f"PDF vazio ou não processável: {filepath}")
                return None

            return text

        except Exception as e:
            logging.error(f"Erro ao ler PDF {filepath}: {e}")
            return None

    # ---------- Detecção de idioma ----------
    def detect_language(self, text: str) -> str:
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Detecte o idioma. Responda apenas 'pt' ou 'en'."},
                    {"role": "user", "content": text}
                ],
                max_tokens=5,
                temperature=0
            )
            result = response.choices[0].message.content.lower()
            return "pt" if "pt" in result else "en"
        except Exception as e:
            logging.error(f"Erro na detecção de idioma: {e}")
            return "unknown"

    # ---------- Resumo ----------
    def summarize(self, text: str, language: str) -> str:
        if not text:
            return "❌ Texto vazio, não é possível gerar resumo."
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": f"Resuma no idioma {language}:\n{text}"}
                ],
                max_tokens=800,
                temperature=0.3
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logging.error(f"Erro na sumarização: {e}")
            return "❌ Erro ao gerar resumo."

    # ---------- Resposta à pergunta ----------
    def answer_question(self, question: str, summary: str, language: str) -> str:
        if not question or not summary:
            return "❌ Pergunta ou resumo vazio, impossível gerar resposta."
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": f"Com base no resumo ({language}), responda à pergunta:\nResumo:\n{summary}\nPergunta: {question}"}
                ],
                max_tokens=500,
                temperature=0.3
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logging.error(f"Erro ao gerar resposta: {e}")
            return "❌ Erro ao gerar resposta."

    # ---------- Salvando arquivos ----------
    def save_summary_txt(self, summary: str, prefix: str = "summary") -> str | None:
        try:
            if not os.path.exists("outputs"):
                os.makedirs("outputs")
            safe_prefix = "".join(c for c in prefix if c.isalnum() or c in "_-")
            path = f"outputs/{safe_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(path, "w", encoding="utf-8") as f:
                f.write(summary)
            return path
        except Exception as e:
            logging.error(f"Erro ao salvar TXT: {e}")
            return None

    def save_summary_docx(self, summary: str, prefix: str = "summary") -> str | None:
        try:
            if not os.path.exists("outputs"):
                os.makedirs("outputs")
            safe_prefix = "".join(c for c in prefix if c.isalnum() or c in "_-")
            path = f"outputs/{safe_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
            doc = Document()
            doc.add_paragraph(summary)
            doc.save(path)
            return path
        except Exception as e:
            logging.error(f"Erro ao salvar DOCX: {e}")
            return None
