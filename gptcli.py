
import requests
import sys

def get_response(prompt):
    """Gets a response from the OpenAI API."""
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }
    data = {
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 100,
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # This will raise an exception if the response contains an HTTP error status code
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while contacting the API: {e}")
        sys.exit(1)

    return response.json()["choices"][0]["text"]

def main():
    """The main function."""
    if len(sys.argv) < 2:
        print("Usage: chatgpt <prompt>")
        sys.exit(1)

    prompt = sys.argv[1]
    response = get_response(prompt)
    print(response)

if __name__ == "__main__":
    main()
