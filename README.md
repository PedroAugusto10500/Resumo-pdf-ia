# 📄 Resumo Inteligente de PDFs com IA

<p align="center">
  <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-28a745?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Tecnologia-IA%20(OpenAI)-412991?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Gradio-UI%20Interativa-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Licença-MIT-green?style=for-the-badge" />
</p>

---

# Aplicação Inteligente de Resumo de PDFs

Esta ferramenta lê PDFs, extrai texto página por página, detecta automaticamente o idioma e gera resumos completos usando IA da OpenAI. Os resumos podem ser combinados, permitindo que o usuário faça perguntas ao conteúdo e receba respostas claras e precisas. É possível baixar os resultados em TXT ou DOCX, tornando o processo rápido e prático.  

O projeto demonstra integração prática com modelos de IA, automação em Python, criação de interfaces interativas com Gradio e aumento de produtividade no processamento de documentos extensos.  

A aplicação é ideal para estudantes que precisam resumir PDFs acadêmicos, profissionais revisando relatórios ou pesquisadores analisando múltiplos documentos, oferecendo uma forma objetiva e eficiente de interpretar conteúdos longos.

---

## 📸 Demonstração

<div align="center">
<table>
  <tr>
    <td align="center">
      <b>Interface Principal - Modo Escuro</b><br>
      <img src="https://github.com/PedroAugusto10500/Resumo-pdf-ia/blob/main/agents/prints/Captura%20de%20tela%202025-11-28%20090214.png" width="400">
    </td>
    <td align="center">
      <b>Interface Principal - Modo Claro</b><br>
      <img src="https://github.com/PedroAugusto10500/Resumo-pdf-ia/blob/main/agents/prints/Captura%20de%20tela%202025-11-28%20091031.png" width="400">
    </td>
  </tr>
</table>
</div>

---

## 💡 Funcionalidades

### 📥 Processamento de PDFs
- Envie **um ou vários PDFs** simultaneamente  
- Extração de texto **página por página**  

### 🤖 Inteligência Artificial (OpenAI)
- **Detecção automática do idioma** (pt/en)  
- Geração de **resumos inteligentes e coerentes**  
- **Respostas a perguntas** baseadas nos resumos  
- Texto limpo, direto e fácil de ler  

### 📤 Exportação
- Baixe resumos em **TXT** ou **DOCX**  
- Histórico de conversas **via Chatbot integrado**

### 🎨 Interface Moderna (Gradio)
- Layout **limpo, responsivo e intuitivo**  
- Suporte a **múltiplos arquivos**  

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologias | Descrição |
|--------|-------------|-----------|
| **IA** | OpenAI GPT-4.1 / GPT-4o-mini | Geração de resumos e respostas inteligentes |
| **Interface** | Gradio | UI interativa e responsiva |
| **Linguagem** | Python 3.10 | Backend do projeto |
| **PDF** | PyPDF2 | Extração de texto de arquivos PDF |
| **Documentos** | python-docx | Exportação de resumos em DOCX |
| **Configuração** | python-dotenv | Gerenciamento seguro de API Key |

---

## ⚙️ Como Executar o Projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio
cd seu-repositorio
```
2️⃣ Criar e ativar ambiente virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```
3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```
4️⃣ Criar arquivo .env
```bash
OPENAI_API_KEY=sua_chave_aqui
```
5️⃣ Executar o projeto
```bash
python app.py

A aplicação abrirá em:
http://localhost:7861
```
