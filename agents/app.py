import gradio as gr
from src.my_agent.agent import Agent
from src.my_agent.history_manager import HistoryManager
from src.my_agent.processor import process_pdfs
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

agent = Agent()

# Converte histórico persistente do JSON → formato que o Chatbot entende
def convert_history_for_chatbot(history_json):
    gradio_format = []
    for entry in history_json:
        gradio_format.append((entry["question"], entry["answer"]))
    return gradio_format

loaded_history = convert_history_for_chatbot(agent.history_manager.load_history())

# Função que conecta backend ao Gradio, agora com tratamento de erro e status
def gradio_process_pdfs_enhanced(files, question, history):
    if not files:
        return "⚠️ Nenhum arquivo enviado.", history, None, None, "Erro: envie ao menos um PDF."
    if not question.strip():
        return "⚠️ Pergunta vazia.", history, None, None, "Erro: insira uma pergunta."

    try:
        status_message = "⏳ Processando PDFs..."
        # Processamento real
        summary, updated_history, txt_path, docx_path = process_pdfs(agent, files, question, history)
        status_message = "✅ Processamento concluído!"
        
        # Tornar histórico mais informativo
        pdf_names = ", ".join([f.name for f in files])
        history_entry = f"📄 {pdf_names}\n❓ {question}\n💬 {summary}"
        updated_history.append((question, summary))
        
        return summary, updated_history, txt_path, docx_path, status_message

    except Exception as e:
        logging.error(f"Erro no processamento: {e}")
        return "❌ Ocorreu um erro ao processar os PDFs.", history, None, None, "Erro no processamento. Veja logs."

# ---------------- Interface Gradio ----------------
with gr.Blocks(title="Resumo Inteligente de PDFs") as demo:
    gr.Markdown(
        "# 📄 Sistema Inteligente de Resumo de PDFs\n"
        "Envie PDFs, faça perguntas e receba um resumo automático."
    )

    with gr.Row():
        # Inputs
        with gr.Column(scale=1):
            pdf_input = gr.File(
                label="📤 Envie seus PDFs",
                file_types=[".pdf"],
                file_count="multiple"
            )
            question_input = gr.Textbox(
                label="❓ Pergunta",
                lines=2,
                placeholder="Ex.: Quais são os principais pontos?"
            )
            submit_btn = gr.Button(
                "✨ Gerar Resumo e Resposta",
                variant="primary"
            )

            # Histórico persistente
            history_state = gr.State(loaded_history)

        # Outputs
        with gr.Column(scale=2):
            output_text = gr.Textbox(
                label="📘 Resumo + Resposta",
                lines=20,
                interactive=False,
                show_copy_button=True
            )

            chatbot = gr.Chatbot(
                label="💬 Histórico",
                value=loaded_history,
                height=400
            )

            status_box = gr.Textbox(
                label="Status",
                interactive=False
            )

            with gr.Accordion("📄 Baixar Resumos", open=True):
                with gr.Row():
                    txt_output = gr.File(label="TXT")
                    docx_output = gr.File(label="DOCX")

    submit_btn.click(
        fn=gradio_process_pdfs_enhanced,
        inputs=[pdf_input, question_input, history_state],
        outputs=[output_text, chatbot, txt_output, docx_output, status_box]
    )

demo.launch(server_port=7861)
