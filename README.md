# 📄 Resumo Inteligente de PDFs com IA

<p align="center">
  <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-28a745?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Tecnologia-IA%20(OpenAI)-412991?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Gradio-UI%20Interativa-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Licença-MIT-green?style=for-the-badge" />
</p>

Uma aplicação inteligente capaz de **ler PDFs, gerar resumos automáticos e responder perguntas** com base nas informações extraídas — utilizando **IA da OpenAI**, interface **Gradio** e processamento local de texto.  

Ideal para estudo, produtividade e demonstração de domínio em **Integração com IA, Python e soluções práticas**.

---

## 📸 Demonstração

> GIF ou vídeo curto é ideal para mostrar upload → resumo → resposta.  
> Substitua as imagens abaixo por prints reais.

<div align="center">
<table>
  <tr>
    <td align="center">
      <b>Interface Principal</b><br>
      <img src="prints/interface.png" width="400">
    </td>
    <td align="center">
      <b>Histórico de Conversa</b><br>
      <img src="prints/chat.png" width="400">
    </td>
  </tr>
  <tr>
    <td align="center" colspan="2">
      <b>Resumos e Downloads</b><br>
      <img src="prints/downloads.png" width="450">
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
## 🧠 Como Funciona
O usuário envia PDFs

O sistema extrai o texto página por página

A IA detecta o idioma e gera resumos

Todos os resumos são combinados

Perguntas podem ser feitas com base no resumo

Resultados podem ser baixados em TXT ou DOCX


## ⭐ Observações Finais
Este projeto demonstra:

Integração prática com modelos de IA

Processamento de arquivos PDF

Criação de interfaces interativas com Gradio

Aplicação de Python no mundo real

Automação e produtividade

### Casos de uso sugeridos:
Estudantes resumindo artigos e PDFs acadêmicos

Profissionais revisando relatórios
