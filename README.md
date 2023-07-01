
bash terminal app that allows access to a model of OpenAI and allows you to work with a chat box via CLI with GPT:

```Python
import requests
import sys

def get_response(prompt):
    """Gets a response from the OpenAI API."""
    url = "https://api.openai.com/v1/engines/gpt-3/completions"
    params = {
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 100,
    }
    response = requests.post(url, json=params)
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
```
Use code with caution. Learn more
This code first imports the requests and sys modules. The requests module is used to make HTTP requests to the OpenAI API, and the sys module is used to get the command-line arguments.

The get_response() function takes a prompt as input and returns a response from the OpenAI API. The url variable specifies the URL of the OpenAI API endpoint, and the params variable specifies the parameters of the request. The response variable is a JSON object that contains the response from the API. The choices key of the JSON object contains a list of possible responses, and the text key of each response contains the text of the response.

The main() function is the main function of the program. It first checks to make sure that the user has provided a prompt. If the user has not provided a prompt, the program prints a usage message and exits.

If the user has provided a prompt, the main() function calls the get_response() function to get a response from the OpenAI API. The response is then printed to the console.

To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as chatgpt.py, you can run it by typing the following command into the terminal:

```
python3 chatgpt.py "What is the meaning of life?"
```
Use code with caution!
