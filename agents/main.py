import gradio as gr
from src.my_agent.agent import Agent
from src.utils.email_utils import send_email
from PyPDF2 import PdfReader

agent = Agent()

def pdf_chat(file, question, history):
    if file is None:
        return "Please upload a PDF file.", history, None, None

    if not question or question.strip() == "":
        return "Please enter a question.", history, None, None

    try:
        text = agent.read_pdf(file.name)
    except Exception as e:
        return f"Error reading PDF: {e}", history, None, None

    # Detect language of the question
    lang = agent.detect_language(question)

    # Read page count
    reader = PdfReader(file.name)
    page_count = len(reader.pages)

    # Summarize and answer in detected language
    summary = agent.summarize(text, language=lang)
    answer = agent.answer_question(question, summary, language=lang)

    # Save files
    txt_file = agent.save_summary_txt(summary)
    docx_file = agent.save_summary_docx(summary)

    # Update chat history
    if history is None:
        history = []
    history.append((question, answer))

    # Format result
    result = f"📄 PDF loaded with {page_count} pages.\n\n--- Summary ({lang}) ---\n{summary}\n\n--- Answer ---\n{answer}"

    return result, history, txt_file, docx_file

# Modern and clean Gradio interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, sans-serif;
            background-color: #f9f9f9;
        }
        .gradio-container {
            max-width: 1100px;
            margin: auto;
        }
    </style>
    <div style="text-align: center; padding-top: 30px; padding-bottom: 20px;">
        <h1 style="font-size: 2.5rem; font-weight: 600; color: #2c2c2c;">PDF Assistant</h1>
        <p style="font-size: 1.1rem; color: #666;">Summarize, Ask, and Translate Automatically</p>
    </div>
    """)

    with gr.Row(equal_height=True):
        with gr.Column(scale=1, min_width=320):
            with gr.Group():
                pdf_input = gr.File(label="Upload PDF", file_types=[".pdf"])
                question_input = gr.Textbox(label="Ask a question", placeholder="Ask in English or Portuguese...", lines=2)
                submit_btn = gr.Button("Submit", variant="primary")
                history_state = gr.State([])

        with gr.Column(scale=2):
            output = gr.Textbox(label="Summary & Answer", lines=18, interactive=False)
            chatbot = gr.Chatbot(label="Conversation History")
            with gr.Row():
                download_txt = gr.File(label="Download TXT")
                download_docx = gr.File(label="Download DOCX")

    submit_btn.click(
        fn=pdf_chat,
        inputs=[pdf_input, question_input, history_state],
        outputs=[output, chatbot, download_txt, download_docx]
    )

demo.launch()
