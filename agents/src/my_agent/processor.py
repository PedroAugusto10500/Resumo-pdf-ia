# src/my_agent/processor.py

import os
from datetime import datetime

MAX_FILE_SIZE_MB = 20
MAX_HISTORY = 20

def process_pdfs(agent, files, question, history, status_label=None):

    if not files:
        return "❌ Envie pelo menos um PDF.", history, None, None

    if not question.strip():
        return "❌ Digite uma pergunta.", history, None, None

    lang = agent.detect_language(question)
    full_summary = ""
    summaries = []

    # --- VALIDATION ---
    def validate_pdf(file):
        if not file.name.endswith(".pdf"):
            return False, "❌ Apenas PDFs."
        if os.path.getsize(file.name) > MAX_FILE_SIZE_MB * 1024 * 1024:
            return False, f"❌ Máximo {MAX_FILE_SIZE_MB}MB."
        return True, ""

    # --- CHUNK SUMMARY ---
    def summarize_large_text(agent, text, language, chunk_size=2000):
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        partials = []

        for i, ch in enumerate(chunks):
            summary = agent.summarize(ch, language)
            partials.append(f"[Parte {i+1}]\n{summary}")

        return agent.summarize("\n".join(partials), language)

    # --- PDF PROCESS ---
    def read_and_summarize_pdf(agent, file_path, language):
        text = agent.read_pdf(file_path)
        if not text:
            return "❌ Não foi possível extrair texto."
        return summarize_large_text(agent, text, language)

    # --- LOOP FILES ---
    for idx, file in enumerate(files):

        valid, msg = validate_pdf(file)
        if not valid:
            return msg, history, None, None

        summary = read_and_summarize_pdf(agent, file.name, lang)
        summaries.append(f"📄 {file.name}:\n{summary}")
        full_summary += summary + "\n\n"

    # --- FINAL ANSWER ---
    final_summary = "\n\n".join(summaries)
    answer = agent.answer_question(question, final_summary, lang)

    # --- PERSIST HISTORY ---
    agent.history_manager.add_entry(question, answer)
    history.append((question, answer))

    if len(history) > MAX_HISTORY:
        history = history[-MAX_HISTORY:]

    # --- SAVE OUTPUT FILES ---
    txt_path = agent.save_summary_txt(final_summary)
    docx_path = agent.save_summary_docx(final_summary)

    result_text = (
        f"Resumo Geral:\n{final_summary}\n\n"
        f"Resposta:\n{answer}\n\n"
        f"Arquivos salvos:\nTXT: {txt_path}\nDOCX: {docx_path}"
    )

    return result_text, history, txt_path, docx_path
