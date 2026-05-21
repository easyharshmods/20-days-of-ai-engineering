# Day 07 - Streamlit AI App

## What we are building

Today we are building the first web UI in the series: a local Streamlit app that sends a prompt to Ollama and displays the response in the browser.

The app lets you enter an engineering topic, choose a response style, and generate an explanation with the pinned `llama3.2:3b` model.

## Why this matters for AI engineering

Many AI engineering projects start as command-line scripts and quickly need a simple interface for testing. Streamlit is useful because it lets engineers build a local web app without writing frontend JavaScript.

For DevOps and cloud engineers, this is like putting a small internal tool in front of an automation script. The underlying logic still matters, but the UI makes it easier to test and share.

## Concepts covered

- Streamlit app structure
- Text input
- Selectbox options
- Buttons
- Basic loading state
- Ollama integration
- Local-only security trade-offs

## Folder structure

```text
day-07-streamlit-ai-app/
  README.md
  requirements.txt
  code/
    app.py
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
cd day-07-streamlit-ai-app
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

`code/llm_client.py` contains the local Ollama request logic and prompt builder.

`code/app.py` contains the Streamlit interface:

- `st.text_input()` collects the topic.
- `st.selectbox()` chooses the explanation style.
- `st.button()` triggers the model call.
- `st.spinner()` shows that the local model is working.
- `st.error()` displays connection or model errors.

The app avoids secrets and cloud services. Prompts are sent to local Ollama on your machine.

## Run the project

From inside `day-07-streamlit-ai-app`, with the virtual environment activated:

```bash
streamlit run code/app.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

Streamlit should open a browser page with:

- a title
- a topic input
- a response style selector
- a generate button
- an answer area

Try this topic:

```text
why API retries need backoff
```

The answer should come from:

```text
llama3.2:3b
```

## Common issues and fixes

**`streamlit: command not found`**

Install dependencies inside the lesson virtual environment:

```bash
pip install -r requirements.txt
```

**Ollama connection fails**

Start Ollama and pull the pinned model:

```bash
ollama pull llama3.2:3b
```

**The app is slow**

Local models depend on CPU and memory. Close heavy applications and confirm Ollama is not loading multiple models at the same time. The default `llama3.2:3b` is intentionally small to stay laptop-friendly.

If you have more RAM available and want to try a more capable alternative model (heavier, ~9.6 GB):

```bash
ollama pull gemma4:latest
```

Then edit `DEFAULT_MODEL` in `code/llm_client.py`.

## What would change in production

In production, you would add authentication, rate limits, request logging, input limits, monitoring, and a clearer deployment boundary for the model runtime.

You would also review what prompts and responses are stored. Even local uploaded or typed data can contain sensitive information.

## Key takeaways

- Streamlit is useful for fast local AI app testing.
- The UI should call reusable Python logic, not hide all logic in page code.
- Local Ollama keeps this lesson self-contained.
- Buttons, inputs, and loading states make the model call easier to test.
- A local demo still needs production-minded security thinking.

## Next step

In Day 08, we will turn this single-turn app into a chat UI with session memory.
