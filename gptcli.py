import requests
import sys

API_KEY = "sk-..........................................."
API_URL = "https://api.openai.com/v1/chat/completions"

def get_response(prompt):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 200
    }
    try:
        r = requests.post(API_URL, headers=headers, json=data)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        sys.exit(f"API Error: {e}")

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: chatgpt <prompt>")
    print(get_response(" ".join(sys.argv[1:])))

if __name__ == "__main__":
    main()
