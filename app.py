"""
Simple AI Chatbot - Ollama + Streamlit
----------------------------------------
A beginner-friendly project that connects a local Ollama model
to a simple Streamlit chat interface.

Requirements before running:
1. Install Ollama: https://ollama.com/download
2. Pull a model, e.g.:  ollama pull llama3
3. Make sure Ollama is running (it usually starts automatically,
   or run `ollama serve` in a terminal).
4. Install Python packages:  pip install -r requirements.txt
5. Run the app:  streamlit run app.py
"""

import streamlit as st
import ollama

# ----------------------------
# Page setup
# ----------------------------
st.set_page_config(page_title="Simple AI Chatbot", page_icon="🤖")
st.title("🤖 Simple AI Chatbot (Ollama + Streamlit)")
st.caption("Ask me anything! Powered by a local Ollama model.")

# ----------------------------
# Sidebar settings
# ----------------------------
st.sidebar.header("Settings")
model_name = st.sidebar.text_input(
    "Ollama model name",
    value="llama3",
    help="Must be a model you've already pulled with `ollama pull <model>`."
)
st.sidebar.markdown(
    "Examples: `llama3`, `gemma:2b`, `mistral`\n\n"
    "Run `ollama list` in your terminal to see installed models."
)

# ----------------------------
# Chat history (session state)
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ----------------------------
# Handle new user input
# ----------------------------
prompt = st.chat_input("Type your question or prompt here...")

if prompt:
    # Show and store the user's message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from Ollama
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = ollama.chat(
                    model=model_name,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                answer = response["message"]["content"]
            except Exception as e:
                answer = (
                    f"⚠️ Error contacting Ollama model '{model_name}'.\n\n"
                    f"Details: {e}\n\n"
                    "Make sure Ollama is running and the model has been "
                    "pulled (e.g. `ollama pull llama3`)."
                )
        st.markdown(answer)

    # Store assistant's reply
    st.session_state.messages.append({"role": "assistant", "content": answer})

# ----------------------------
# Clear chat button
# ----------------------------
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
