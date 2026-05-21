# Day 08 - Chat UI and Session Memory

## What we are building

Today we are building a local chat assistant with Streamlit and Ollama.

Unlike Day 07, this app keeps a conversation history in `st.session_state`. Each new user message is sent to `llama3.2:3b` along with the recent conversation so the model can respond with basic session context.

## Why this matters for AI engineering

Most useful AI assistants are not single-turn forms. Users expect a conversation: they ask a question, clarify, correct, and continue.

Session memory is the first step toward that behavior. It is not long-term memory or a database. It is temporary state for one browser session, similar to keeping request context while a tool is open.

The analogy for this lesson is an incident chat room. The assistant needs the latest messages to understand what "that error" or "the previous service" refers to.

## Concepts covered

- `st.chat_input`
- `st.chat_message`
- `st.session_state`
- Conversation history
- Prompt construction from recent messages
- Local-only memory trade-offs

## Folder structure

```text
day-08-chat-ui-and-session-memory/
  README.md
  requirements.txt
  code/
    app.py
    chat_logic.py
    llm_client.py
```

## Prerequisites

- Python 3.14.5
- Ollama installed and running
- The pinned default model:

```bash
ollama pull llama3.2:3b
```

Optional more capable alternative model (heavier, needs more RAM):

```bash
ollama pull gemma4:latest
```

The app uses `llama3.2:3b` by default.

## Setup

Run these commands from the repository root:

```bash
cd day-08-chat-ui-and-session-memory
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

The app has three main files:

- `chat_logic.py` defines the message shape and builds the prompt from recent messages.
- `llm_client.py` calls the local Ollama generate API.
- `app.py` renders the Streamlit chat UI and stores messages in `st.session_state`.

The app stores messages as dictionaries with two fields:

- `role`: either `user` or `assistant`
- `content`: the message text

For each user message, the app builds a prompt using the recent conversation, calls Ollama, appends the assistant response, and renders the full session history.

## Run the project

From inside `day-08-chat-ui-and-session-memory`, with the virtual environment activated:

```bash
streamlit run code/app.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

The browser should show a local chat app. Try:

```text
What is a deployment rollback?
```

Then follow up with:

```text
When would I use it during an incident?
```

The assistant should respond using the session context.

## Common issues and fixes

**Chat history disappears after refresh**

That is expected. `st.session_state` is temporary browser-session memory, not a database.

**Ollama connection fails**

Start Ollama and pull the pinned model:

```bash
ollama pull llama3.2:3b
```

**The assistant seems to forget older messages**

This lesson sends only recent messages to keep prompts small. Larger memory systems need retrieval or storage, which we will introduce later.

## What would change in production

Production chat systems need authentication, durable storage if history matters, retention rules, redaction, rate limits, model monitoring, and careful prompt size controls.

You would also avoid storing sensitive conversation history without a clear policy. Uploaded files and chat text can contain credentials, customer data, or incident details.

## Key takeaways

- `st.session_state` stores temporary UI state.
- Chat messages need a simple role/content structure.
- Session memory is not the same as long-term memory.
- Sending recent conversation helps follow-up questions.
- Prompt size grows as chat history grows.

## Next step

In Day 09, we will add file upload support so the assistant can answer questions about uploaded text files.
