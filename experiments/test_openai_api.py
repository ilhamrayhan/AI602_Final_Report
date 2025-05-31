"""
test_openai_api.py

Utility script to test Open AI API Calls.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()
client = OpenAI()

def test_openai_api():
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "Hello, can you confirm that the API key is working?"}],
            max_tokens=20
        )
        print("API key test successful!")
        print("Response:", completion.choices[0].message.content.strip())
    except Exception as e:
        print("API key test failed:")
        print(e)

if __name__ == "__main__":
    test_openai_api()

    


