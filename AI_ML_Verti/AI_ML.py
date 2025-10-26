# Devsoc AI/ML Vertical Project
#
# Name- Harita Suthar
#
#
# Requirements for running the code:
# 1) Set an API key from Google AI Studio as an environment variable named MY_API_KEY.
# 2) Install genai and package requests from it
# 
#

import os
import json
from google import genai

API_KEY = os.environ.get("MY_API_KEY")
if not API_KEY:
    raise ValueError("Environment variable MY_API_KEY not found. Please set it before running.")

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.5-flash"

INPUT_FILE = r"C:\Users\hemang suthar\Desktop\BITS Sem-1\Devsoc\text.txt"

OUTPUT_FILE = "responses.json"


if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"Could not find the input file: {INPUT_FILE}\n"
                            f"Current working directory: {os.getcwd()}")


with open(INPUT_FILE, "r", encoding="utf-8") as f:
    prompts = [line.strip() for line in f if line.strip()]

responses = []

print(f"Starting to process {len(prompts)} prompts...\n")

for i, prompt in enumerate(prompts, start=1):
    try:
        response = client.models.generate_content(  
            model=MODEL,
            contents=prompt
        )

        responses.append({
            "prompt": prompt,
            "response": response.text.strip()
        })

        print(f" Done with question {i}/{len(prompts)}: {prompt}")

    except Exception as e:
        responses.append({
            "prompt": prompt,
            "response": f"ERROR: {e}"
        })
        print(f" Error with question {i}: {e}")


with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(responses, f, indent=4, ensure_ascii=False)

print(f"\n All {len(prompts)} prompts processed successfully!")
print(f" Responses saved to: {os.path.abspath(OUTPUT_FILE)}")
