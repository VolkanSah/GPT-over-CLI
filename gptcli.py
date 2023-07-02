# GPT API over CLI
import subprocess
import sys
import json
def call_api(prompt):
    """Calls the OpenAI API using cURL."""
    data = {
        "model": "gpt-3.5-turbo-16k",
        "messages": [{"role": "system", "content": "You are a helpful assistant."}, 
                     {"role": "user", "content": prompt}]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer sk-........................................."
    }
    command = [
        "curl",
        "https://api.openai.com/v1/chat/completions",
        "-X", "POST",
        "-H", json.dumps(headers),
        "-d", json.dumps(data)
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def main():
    """The main function."""
    if len(sys.argv) < 2:
        print("Usage: chatgpt <prompt>")
        sys.exit(1)

    prompt = sys.argv[1]
    response = call_api(prompt)
    print(response)

if __name__ == "__main__":
    main()
# VolkanSah
