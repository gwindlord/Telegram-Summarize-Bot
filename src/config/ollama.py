MODEL = 'llama3.2:1b'

THREADS = 8

START_SENTENCE = "Here is a summary of the chat messages sent after the message you replied to:"

SYSTEM_PROMPT = f"""
Summarize the main points of the chat messages. Start with: \"{START_SENTENCE}\".
"""
