# GPT-over-CLI

##### Update 2025/10

**GPT-over-CLI** is a lightweight and simple command-line interface (CLI) for interacting with OpenAI's modern GPT models such as GPT-4o and GPT-5.
It provides a quick and minimal way to generate responses right from your terminal — ideal for developers, researchers, and automation workflows.

## Features

* **Updated API:** Uses the latest `/v1/chat/completions` endpoint (compatible with GPT-4 and GPT-5).
* **Lightweight:** No dependencies beyond `requests`.
* **Simple:** Pass a prompt, get a response.
* **Customizable:** Adjust model, temperature, and token limits easily in code.

## Usage

1. Clone this repository.
2. Install dependencies:

   ```bash
   pip install requests
   ```
3. Add your OpenAI API key to your environment variables:

   ```bash
   export OPENAI_API_KEY="your_api_key"
   ```

   Or replace it directly in the script.
4. Run the CLI:

   ```bash
   python3 gptcli.py "your prompt here"
   ```

## Disclaimer

This tool is for development and research purposes only.
Use responsibly and follow OpenAI’s usage policies.
Do **not** expose your API key publicly.

## Contribution

Contributions, bug reports, and feature suggestions are welcome — open an issue or pull request anytime.

## Credits

[Volkan Kücükbudak](https://github.com/volkansah)

