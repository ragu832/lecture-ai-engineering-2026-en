"""Lecture 01: a script that asks a bare LLM questions in one conversation.

Usage:
    uv run python -m app.ask "What is LoRA?"
    uv run python -m app.ask            # Ask the default question, then continue with follow-ups

A "bare" call with no tools, but with conversation history for follow-up questions.
Check that, when asked about course-specific information, it either says "I don't know"
or gives a plausible general answer (which differs from the actual course).
(In Lecture 03, improve it by making an agent that can search the glossary.)
"""

import argparse

from google import genai
from google.genai import errors

from app.config import MODEL, api_error_message, get_api_key

# A course-specific question. The correct answer is in homework-levels in data/glossary.json
DEFAULT_QUESTION = "What are the 3 homework levels in the AIE2026 course?"


def ask(question: str, chat=None) -> str:
    if chat is None:
        client = genai.Client(api_key=get_api_key())
        chat = client.chats.create(model=MODEL)

    response = chat.send_message(question)

    usage = response.usage_metadata
    print(f"[input tokens] {usage.prompt_token_count}")
    print(f"[output tokens] {usage.candidates_token_count}")

    return response.text


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask a bare LLM questions in one conversation")
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    args = parser.parse_args()

    print(f"[model] {MODEL}")
    try:
        client = genai.Client(api_key=get_api_key())
        chat = client.chats.create(model=MODEL)

        question = args.question
        while True:
            print(f"[question] {question}\n")
            print(ask(question, chat))
            try:
                question = input("\n[follow-up] ")
            except EOFError:
                break
            if question.strip().lower() in {"exit", "quit"}:
                break
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
