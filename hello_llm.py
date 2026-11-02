
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

model = "openai/gpt-oss-120b"

role = "user"

prompt = "Do you know Padho with Pratyush?"

message = {
    "role": role,
    "content": prompt
}

messages = [message]

try:
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    answer = response.choices[0].message.content

    print("\nLLM Response:")
    print(answer)

except Exception as e:
    print("Error occurred:", e)
