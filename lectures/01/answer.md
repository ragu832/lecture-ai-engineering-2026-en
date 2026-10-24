# Lecture 01 Answers

## Exercises

- Model's answer to the course-specific question (the 3 homework levels; a summary is fine):
- What you noticed when comparing it with the correct meaning in the glossary:
- Token counts you displayed (input / output):

## Homework

- Level attempted: Implementation
- What you did: Updated ask.py to use a persistent Gemini chat session.
- Results: Now I can ask follow up questions and with exit, quit or ctrl+D to end the conversation.
- Observations and questions: Persistent chat session allows model to remember earlier questions and making follow up questions, but I wonder about how long should conversation history be retained? What happens when the conversation becomes too long? How could old messages be summarized to reduce token usage?