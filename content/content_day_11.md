# Day 11 Content Package

## video_title

Prompt Engineering for Engineers - Day 11

## thumbnail_text

Prompt Templates for Engineers

## description

In Day 11 of 20 Days of AI Engineering, we treat prompts the way we treat any other interface: structured, reviewable, and reusable.

We build three prompt modes that map to real cloud engineering work. An AWS explainer that returns a definition, why it matters, a trade-off, and an example. A Terraform reviewer that scans a snippet and reports what looks fine, what is risky, and what to improve. An incident summarizer that produces an impact, likely cause, timeline highlights, and follow-up actions. A small `build_prompt` dispatcher routes a mode to the right template, then sends the result to local Ollama with `llama3.2:3b`.

The point of this lesson is not to call an LLM. We have done that since Day 05. The point is to stop sending unstructured user text into the model and start sending designed prompts that ask for the answer in a shape your team can read.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What we are building
- 00:00 Why prompts are interfaces
- 00:00 Prompt modes and the dispatcher
- 00:00 AWS explainer template
- 00:00 Terraform reviewer template
- 00:00 Incident summarizer template
- 00:00 Run the project with the Terraform sample
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# Prompt Engineering for Engineers

## Hook

Most "AI tools" inside engineering teams are one big text box and a model call.

That works for a demo, but as soon as the assistant has multiple jobs, the answers stop being consistent, and nobody can review the prompt because it lives in a UI string somewhere.

Today we fix that.

## Intro

Welcome to Day 11 of 20 Days of AI Engineering.

So far we have called Ollama, built a chat UI, added file upload, and summarized PDFs. The model has been doing most of the thinking. Today, the prompt does its share.

We are going to build three prompt modes that match real cloud engineering tasks: an AWS explainer, a Terraform reviewer, and an incident summarizer. Then a single `build_prompt` function picks the right template based on the mode.

## Concept Explanation

A prompt template is an interface. It documents what the model is being asked to do, in what role, against what input, and in what shape the answer should come back.

When prompts live inside UI code or random scripts, they are invisible to the team. They cannot be reviewed, diffed, or versioned. The model's behavior drifts because the input drifts.

When prompts live in their own module, they look like any other piece of code. A reviewer can read them. A future you can change them. A test can lock the shape of the answer.

For a cloud engineer, this is like moving from a one-off shell script to a small, well-named function with a clear contract.

## Hands-on Build

Open `code/prompt_templates.py`.

There is a `PromptMode` literal type with three values: `aws_explainer`, `terraform_reviewer`, and `incident_summarizer`. Using a literal here is intentional. Misspelling the mode becomes a type error instead of a silent fallback to wrong behavior.

Each mode has its own builder function. `build_aws_explainer_prompt` takes a topic, puts the model in tutor mode, and asks for a numbered structure: definition, why it matters for AI systems, production trade-off, one practical example.

`build_terraform_reviewer_prompt` takes a Terraform snippet, frames the model as a reviewer for a platform team, focuses it on security, reliability, and operational clarity, and asks for what looks reasonable, what is risky, and what to improve.

`build_incident_summarizer_prompt` takes raw incident notes, tells the model to be factual and avoid blame, and asks for impact, likely cause, timeline highlights, and follow-up actions.

The `build_prompt` function is a small dispatcher. It takes a mode and an input string, picks the right template, and raises `ValueError` on an unsupported mode.

Open `code/main.py`. It reads `sample/terraform_snippet.txt`, runs `build_prompt("terraform_reviewer", text)`, calls Ollama through `llm_client.generate_answer`, and prints the response. If the LLM call fails, it prints a clean message instead of a traceback.

Run the project with `python code/main.py`.

## Production Thinking

Once prompts are first-class code, they need the things other code needs.

Version your prompts. A small change to a template can shift the answer shape, so review prompt changes the same way you review schema changes.

Evaluate them. For each mode, write a few inputs and expected answer properties, and check the model's output against them when you change the template or the model.

Be careful with what you send. Terraform snippets, incident notes, and account names can contain sensitive infrastructure detail. Local development is fine. Pushing the same prompts at a hosted model without a data agreement is not.

## Recap

Today we moved prompts out of ad-hoc strings and into a small templates module.

We built three modes that match real cloud engineering work, wired them through a `build_prompt` dispatcher, and ran the Terraform reviewer against a real snippet locally.

Prompts are interfaces. Treat them that way and the assistant becomes something a team can actually review and improve.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 11 locally, swap the mode, point the Terraform reviewer at one of your own snippets, and see how the structure changes the answer.

## pinned_comment

Day 11 builds three prompt modes (`aws_explainer`, `terraform_reviewer`, `incident_summarizer`) with a `build_prompt` dispatcher, then calls local Ollama with `llama3.2:3b`. The point is to treat prompts as a reviewable interface, not a hidden string inside UI code.

## linkedin_post

Day 11 of my 20 Days of AI Engineering series is about prompts as engineering interfaces.

I built three modes for cloud engineering work: an AWS explainer, a Terraform reviewer, and an incident summarizer. A small `build_prompt` dispatcher routes a mode to the right template, then sends it to local Ollama with `llama3.2:3b`.

The lesson is short and the code is small. The takeaway is that once prompts live in their own module, your team can review them, version them, and evaluate them the same way they handle any other code.

## learning_objectives

- Build role-based prompt templates for engineering work.
- Ask the model for output in a structure your team can read.
- Keep prompt logic separate from model-call logic.
- Use a literal type and a dispatcher to switch between modes safely.
- Run a template against a real Terraform snippet locally.

## common_mistakes

- Passing raw user text directly to the model with no role or structure.
- Burying prompts inside Streamlit or FastAPI UI code where they cannot be reviewed.
- Treating prompt changes as casual edits instead of interface changes.
- Sending Terraform, secrets, or account data into a hosted model without checking the data policy.
- Skipping evaluation, so the prompt drifts silently every time the template or model changes.

## expected_output

The script loads `sample/terraform_snippet.txt`, builds a `terraform_reviewer` prompt, calls `llama3.2:3b`, and prints something like:

```text
Prompt mode: terraform_reviewer
1. What looks reasonable
   - The bucket has a public access block with all four settings enabled.
2. Risks or missing controls
   - No server-side encryption configuration is declared.
   - No versioning or lifecycle policy.
   - No access logging.
3. Suggested improvements
   - Add aws_s3_bucket_server_side_encryption_configuration.
   - Enable versioning and define a lifecycle rule.
   - Restrict bucket policy and add logging.
```

The exact wording varies between runs. The shape (reasonable / risks / improvements) should stay consistent because the template enforces it.

If Ollama is not running or the model is not pulled, the script prints a clean message such as `LLM call failed: Could not reach Ollama: ...` instead of a traceback.
