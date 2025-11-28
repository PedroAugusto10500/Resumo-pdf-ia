import gradio as gr
from src.agent.agent import Agent
from src.utils.security import validate_pdf, sanitize
from PyPDF2 import PdfReader

agent = Agent()

# =======================================================
# 📘 Função principal - Agora é a ÚNICA função do backend
# =======================================================
def pdf_chat_with_progress(file, question, history, progress=gr.Progress()):

    progress(0, "Iniciando...")

    # Arquivo obrigatório
    if file is None:
        return "📌 Envie um arquivo PDF.", history, None, None

    # Pergunta obrigatória
    if not question or question.strip() == "":
        return "📌 Digite uma pergunta.", history, None, None

    # Sanitização básica
    question = sanitize(question)

    # Segurança: valida PDF
    try:
        validate_pdf(file)
    except Exception as e:
        return f"⚠️ {e}", history, None, None

    progress(0.2, "Lendo PDF...")

    # Leitura do PDF
    try:
        text = agent.read_pdf(file.name)
    except Exception as e:
        return f"Erro ao ler PDF: {e}", history, None, None

    # Número de páginas
    reader = PdfReader(file.name)
    page_count = len(reader.pages)

    progress(0.4, "Detectando idioma...")

    # Detecção de idioma via IA
    lang = agent.detect_language(question)

    progress(0.6, "Gerando resumo...")

    # Resumo stateless
    summary = agent.summarize(text, language=lang)

    progress(0.8, "Respondendo pergunta...")

    # Pergunta e resposta
    answer = agent.answer_question(question, summary, language=lang)

    # Arquivos para download
    txt_file = agent.save_summary_txt(summary)
    docx_file = agent.save_summary_docx(summary)

    # Histórico da interface
    if history is None:
        history = []
    history.append((question, answer))

    result = (
        f"📄 **PDF carregado com {page_count} páginas.**\n\n"
        f"### 📝 Resumo ({lang}):\n{summary}\n\n"
        f"### 💬 Resposta:\n{answer}"
    )

    progress(1, "Concluído!")

    return result, history, txt_file, docx_file



# =======================================================
# 💠 Interface Gradio - limpa e sem funções duplicadas
# =======================================================
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("""
    <div style="text-align:center; padding:25px;">
        <h1>📘 PDF Assistant IA</h1>
        <p>Resuma PDFs, faça perguntas e exporte o resultado com IA.</p>
    </div>
    """)

    with gr.Row(equal_height=True):
        # Entrada
        with gr.Column(scale=1, min_width=320):
            pdf_input = gr.File(label="📄 Enviar PDF", file_types=[".pdf"], height=150)
            question_input = gr.Textbox(label="💬 Pergunta", placeholder="Faça sua pergunta...")
            submit_btn = gr.Button("Enviar", variant="primary")
            history_state = gr.State([])

        # Saída
        with gr.Column(scale=2):
            output = gr.Textbox(label="Resumo & Resposta", lines=18, interactive=False)
            chatbot = gr.Chatbot(label="Histórico da Conversa")
            
            with gr.Row():
                download_txt = gr.File(label="Baixar TXT")
                download_docx = gr.File(label="Baixar DOCX")

    submit_btn.click(
        fn=pdf_chat_with_progress,
        inputs=[pdf_input, question_input, history_state],
        outputs=[output, chatbot, download_txt, download_docx]
    )

demo.launch()
