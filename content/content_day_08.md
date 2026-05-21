# Day 08 Content Package

## video_title

Chat UI and Session Memory with Streamlit - Day 08

## thumbnail_text

Chat UI + Memory

## description

In Day 08 of 20 Days of AI Engineering, we build a local chat assistant with Streamlit and Ollama.

The app uses `st.chat_input`, `st.chat_message`, and `st.session_state` to keep temporary conversation history. Each new message is sent to local Ollama with recent context using the pinned `llama3.2:3b` model.

This lesson introduces session memory and explains why it is useful, limited, and different from long-term memory or RAG.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What we are building
- 00:00 Session memory explained
- 00:00 Message structure
- 00:00 Streamlit chat UI
- 00:00 Building the chat prompt
- 00:00 Calling Ollama
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# Chat UI and Session Memory with Streamlit

## Hook

A single prompt is useful, but real users usually ask follow-up questions.

If the assistant cannot see the recent conversation, words like "that service" or "the previous error" become hard to answer.

## Intro

Welcome to Day 08 of 20 Days of AI Engineering.

Today we build a local chat assistant with Streamlit and Ollama.

The app keeps temporary session memory using `st.session_state`.

## Concept Explanation

Session memory means the app remembers messages during one browser session.

It is not a database. It is not permanent memory. It is not retrieval.

It is just temporary state that lets the next prompt include recent conversation.

For engineers, this is similar to keeping context in an incident chat while you are actively troubleshooting.

## Hands-on Build

Open `chat_logic.py`.

We define a simple message structure with a role and content.

Then `build_chat_prompt` takes recent messages and turns them into a transcript for the model.

Open `llm_client.py`.

This is the local Ollama client using the pinned `llama3.2:3b` model.

Now open `app.py`.

We initialize `st.session_state.messages` if it does not exist.

We render previous messages using `st.chat_message`.

We collect new input using `st.chat_input`.

When the user sends a message, we append it to session state, build a prompt from recent messages, call Ollama, display the answer, and append the assistant response.

Run the app with `streamlit run code/app.py`.

## Production Thinking

Production memory needs explicit design.

You need to decide what is stored, for how long, who can access it, and how sensitive data is handled.

You also need to manage prompt size. Sending the full chat forever is expensive and eventually breaks context limits.

This lesson keeps memory temporary and local.

## Recap

Today we built a Streamlit chat UI with session memory.

We used role/content messages, `st.session_state`, `st.chat_input`, and `st.chat_message`.

This prepares us for Day 09, where the assistant will answer questions about uploaded files.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 08 locally and ask a follow-up question to see session memory in action.

## pinned_comment

Day 08 adds Streamlit chat UI and temporary session memory. Default model: `llama3.2:3b`. Session memory clears when the app or browser session resets.

## linkedin_post

Day 08 of my 20 Days of AI Engineering series adds chat UI and session memory.

The Streamlit app uses `st.chat_input`, `st.chat_message`, and `st.session_state` to keep recent messages during one local session.

The important distinction: this is temporary session memory, not long-term memory and not RAG.

## learning_objectives

- Build a Streamlit chat interface.
- Store temporary conversation history in `st.session_state`.
- Represent chat messages with role and content.
- Build a prompt from recent conversation.
- Explain the limits of session memory.

## common_mistakes

- Treating session memory as permanent storage.
- Sending unlimited chat history into every prompt.
- Forgetting that refresh or restart can clear state.
- Mixing UI state, prompt logic, and model calls in one function.
- Storing sensitive chat content without a retention policy.

## expected_output

The app opens a local chat UI. It should answer a first question and a follow-up using recent session context.

