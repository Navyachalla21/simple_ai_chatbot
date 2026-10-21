# Simple AI Chatbot (Ollama + Streamlit)

A lightweight, fully local AI chatbot built with **Ollama** and **Streamlit**. It runs a large language model on your own machine, so it needs no cloud API, no API keys, and no internet connection during inference.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Sample Prompts Tested](#sample-prompts-tested)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [What I Learned](#what-i-learned)
- [Author](#author)

---

## Overview

This project demonstrates how to build an end-to-end AI application using a locally hosted language model. A Streamlit web interface captures the user's question, sends it to a local Ollama model, and displays the generated answer in a chat window while keeping the full conversation history.

By default the app uses **TinyLlama** (~1.1B parameters), a compact model that runs comfortably on machines with limited RAM (4 GB or less).

## Features

- Interactive chat interface built with Streamlit's native chat components
- Runs 100% locally, so your prompts never leave your machine
- Persistent conversation history within a session (Streamlit session state)
- Switch models from the sidebar without changing any code (e.g. `tinyllama`, `gemma:2b`, `llama3`, `mistral`)
- One-click **Clear Chat** button to reset the conversation
- Low hardware requirements with the default model

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| Frontend / UI | Streamlit |
| LLM Runtime | Ollama |
| Default Model | TinyLlama (~1.1B parameters) |
| Python Client | `ollama` library |

## How It Works

1. The user types a question into Streamlit's `chat_input` box.
2. The prompt is sent to the local Ollama model through the Python `ollama` library.
3. Ollama runs the model on the local machine and generates a response.
4. The response is displayed in the chat window, and the conversation is stored in `st.session_state` so the history stays on screen.

## Project Structure

```
simple_ai_chatbot/
├── app.py                  # Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── Simple_AI_Chatbot.pdf   # Full project report with screenshots
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.9 or higher
- [Ollama](https://ollama.com/download) installed and running
- At least 4 GB of RAM (for the default TinyLlama model)

### Installation

1. **Clone the repository**

```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   cd YOUR-REPO-NAME
```

2. **Create and activate a virtual environment**

```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
```

   On macOS/Linux:

```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. **Install dependencies**

```bash
   pip install -r requirements.txt
```

4. **Download the model**

```bash
   ollama pull tinyllama
```

## Usage

Start the application:

```bash
streamlit run app.py
```

Then open **http://localhost:8501** in your browser.

- Type a question in the input box at the bottom and press **Enter**.
- Use the sidebar to change the Ollama model name (run `ollama list` in a terminal to see installed models).
- Click **Clear Chat** to start a new conversation.

To use a different model, pull it first and then enter its name in the sidebar:

```bash
ollama pull gemma:2b
```

## Sample Prompts Tested

1. What is Streamlit?
2. Explain Ollama in one line.
3. Give me 3 study tips.
4. What is Python used for?
5. Suggest a healthy breakfast.

Screenshots of these interactions are available in [Simple_AI_Chatbot.pdf](Simple_AI_Chatbot.pdf).

## Limitations

- TinyLlama is a very small model, so answers can occasionally be inaccurate, repetitive, or incomplete. Larger models such as `llama3` or `mistral` give better quality but need more RAM.
- Response speed depends on your hardware (CPU/GPU and available memory).
- Conversation history is stored only for the current session and is lost when the page is refreshed.

## Future Improvements

- Stream responses token by token for a more responsive feel
- Add a system prompt / persona selector
- Save and load chat history to disk
- Add file upload and document Q&A
- Provide model parameter controls (temperature, max tokens)

## What I Learned

- Running a large language model locally with Ollama, without a cloud API
- Building an interactive web UI in Python with Streamlit, including chat components and session state
- How hardware constraints such as available RAM affect which models can run, and the trade-off between model size and response quality
- Connecting a Python backend (Ollama) to a frontend (Streamlit) to create a complete working AI application

## Author

**YOUR NAME**
GitHub: [@YOUR-USERNAME](https://github.com/YOUR-USERNAME)