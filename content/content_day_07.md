# Day 07 Content Package

## video_title

Build a Streamlit AI App with Ollama - Day 07

## thumbnail_text

Streamlit AI App

## description

In Day 07 of 20 Days of AI Engineering, we build the first web UI in the series.

The app uses Streamlit to collect an engineering topic, lets the user choose a response style, sends the prompt to local Ollama with the pinned `llama3.2:3b` model, and displays the answer in the browser.

This lesson shows how to move from command-line LLM scripts to a small local AI application.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What we are building
- 00:00 Why Streamlit helps
- 00:00 App structure
- 00:00 Topic input and style selector
- 00:00 Calling Ollama
- 00:00 Displaying errors and answers
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# Build a Streamlit AI App with Ollama

## Hook

Command-line AI scripts are useful, but they are not always the easiest way to test an idea with another engineer.

Sometimes you need a small local UI before you need a production service.

## Intro

Welcome to Day 07 of 20 Days of AI Engineering.

Today we build a Streamlit app that calls Ollama locally with `llama3.2:3b`.

The app lets us type an engineering topic, choose a style, click a button, and read the model response in the browser.

## Concept Explanation

Streamlit lets Python engineers build local web apps without writing frontend JavaScript.

For AI engineering, that is useful because many prototypes need input boxes, buttons, file uploads, and output areas.

The model call is still normal Python. Streamlit is just the interface around it.

## Hands-on Build

Open `code/llm_client.py`.

This file contains the Ollama endpoint, the pinned model, a prompt builder, a payload builder, and the function that sends the request.

Now open `code/app.py`.

We use `st.title` and `st.caption` for the page header.

`st.text_input` collects the engineering topic.

`st.selectbox` lets the user choose the response style.

`st.button` controls when the model call happens.

Inside the button block, we build the prompt, call Ollama, and display the answer.

Run the app with `streamlit run code/app.py`.

## Production Thinking

A local Streamlit app is good for learning and quick internal demos.

Production needs more: authentication, input limits, rate limits, observability, model availability checks, and a clear policy for prompts and responses.

Local-only does not remove the need to think about sensitive data.

## Recap

Today we moved from terminal output to a local web UI.

We used Streamlit inputs, a selectbox, a button, a loading spinner, and the local Ollama client.

This gives us the foundation for a chat UI in Day 08.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 07 locally and try a few cloud engineering topics.

## pinned_comment

Day 07 builds a local Streamlit app around Ollama. Default model: `llama3.2:3b`. Pull it with `ollama pull llama3.2:3b`.

## linkedin_post

Day 07 of my 20 Days of AI Engineering series moves from command-line scripts to a local web UI.

I built a small Streamlit app that takes an engineering topic, sends a prompt to Ollama with `llama3.2:3b`, and displays the answer in the browser.

The point is simple: AI apps still need clean UI boundaries around reusable Python logic.

## learning_objectives

- Build a small Streamlit app.
- Add text input, selectbox, button, spinner, and output area.
- Call local Ollama from a web UI.
- Keep UI code separate from model-client logic.
- Explain local-only vs production trade-offs.

## common_mistakes

- Running `python code/app.py` instead of `streamlit run code/app.py`.
- Forgetting to install Streamlit.
- Forgetting to start Ollama.
- Putting all model-client logic directly inside the UI file.
- Typing sensitive data into local prototypes without thinking about logs and retention.

## expected_output

The app opens in a browser with a topic input, response style selector, generate button, and answer area.

