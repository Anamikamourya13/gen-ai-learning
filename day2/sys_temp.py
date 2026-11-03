
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# Load .env from current Python file's folder
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# Get API key
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Initialize Groq client
client = Groq(api_key=my_api_key)

# Model name
model = "openai/gpt-oss-120b"

# User role and prompt
role = "user"
prompt = "Explain System Role in LLM with a simple example."

# SYSTEM ROLE: Defines AI behaviour
message_system = {
    "role": "system",
    "content": "You are a helpful AI teacher. Explain every concept in simple language with examples."
}

# USER MESSAGE: Actual user question
message = {
    "role": role,
    "content": prompt
}

# Combine system and user messages
messages = [message_system, message]

# Temperature controls response randomness
temperature = 0.7

try:
    # Send request to Groq API
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )

    # Extract AI response
    answer = response.choices[0].message.content

    print("\n#######################################")
    print("Model:", model)
    print("Temperature:", temperature)
    print("LLM Response:")
    print("#######################################")

    print(answer)

except Exception as e:
    print("Error occurred:", e)
