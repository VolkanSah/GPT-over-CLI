#!/usr/bin/env python3
import argparse
import sys
import json
from typing import Optional
from datetime import datetime

class AIProvider:
    """Base class für AI Provider"""
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def get_response(self, prompt: str, model: str, stream: bool = False) -> str:
        raise NotImplementedError

class OpenAIProvider(AIProvider):
    def get_response(self, prompt: str, model: str = "gpt-4o-mini", stream: bool = False) -> str:
        # TODO: Echte OpenAI API implementieren
        return f"[OpenAI {model}] Dummy response für: {prompt[:50]}..."

class ClaudeProvider(AIProvider):
    def get_response(self, prompt: str, model: str = "claude-sonnet-4", stream: bool = False) -> str:
        # TODO: Echte Anthropic API implementieren
        return f"[Claude {model}] Dummy response für: {prompt[:50]}..."

class GeminiProvider(AIProvider):
    def get_response(self, prompt: str, model: str = "gemini-pro", stream: bool = False) -> str:
        # TODO: Echte Google API implementieren
        return f"[Gemini {model}] Dummy response für: {prompt[:50]}..."

class ConversationHistory:
    """Einfache Conversation History"""
    def __init__(self):
        self.messages = []
    
    def add(self, role: str, content: str):
        self.messages.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
    
    def get_context(self, last_n: int = 5) -> list:
        return self.messages[-last_n:]
    
    def clear(self):
        self.messages = []

class AIChat:
    def __init__(self, config_path: str = "~/.aichat.json"):
        self.providers = {}
        self.history = ConversationHistory()
        self.load_config(config_path)
    
    def load_config(self, path: str):
        """Lädt API Keys aus Config (oder verwendet Dummy)"""
        # TODO: Echte Config laden
        self.providers = {
            "openai": OpenAIProvider("dummy-key"),
            "claude": ClaudeProvider("dummy-key"),
            "gemini": GeminiProvider("dummy-key")
        }
    
    def chat(self, prompt: str, provider: str = "openai", model: Optional[str] = None, 
             stream: bool = False, use_history: bool = False) -> str:
        """Hauptfunktion für Chat"""
        if provider not in self.providers:
            raise ValueError(f"Unknown provider: {provider}")
        
        # History einbauen wenn gewünscht
        if use_history and self.history.messages:
            context = self.history.get_context()
            prompt = self._build_prompt_with_context(prompt, context)
        
        # Response holen
        response = self.providers[provider].get_response(
            prompt, 
            model or self._get_default_model(provider),
            stream
        )
        
        # History updaten
        if use_history:
            self.history.add("user", prompt)
            self.history.add("assistant", response)
        
        return response
    
    def _get_default_model(self, provider: str) -> str:
        defaults = {
            "openai": "gpt-4o-mini",
            "claude": "claude-sonnet-4",
            "gemini": "gemini-pro"
        }
        return defaults.get(provider, "default")
    
    def _build_prompt_with_context(self, prompt: str, context: list) -> str:
        """Baut Prompt mit Conversation Context"""
        context_str = "\n".join([f"{m['role']}: {m['content']}" for m in context])
        return f"Previous conversation:\n{context_str}\n\nCurrent: {prompt}"
    
    def interactive_mode(self, provider: str = "openai"):
        """Interaktiver Chat Modus"""
        print(f"🤖 Interactive mode with {provider} (type 'exit' to quit, 'clear' to reset)")
        print("-" * 60)
        
        while True:
            try:
                user_input = input("\n👤 You: ").strip()
                
                if user_input.lower() == 'exit':
                    break
                if user_input.lower() == 'clear':
                    self.history.clear()
                    print("✨ History cleared")
                    continue
                if not user_input:
                    continue
                
                response = self.chat(user_input, provider, use_history=True)
                print(f"\n🤖 AI: {response}")
                
            except KeyboardInterrupt:
                print("\n\nBye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Multi-AI CLI Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ai "explain quantum computing"
  ai "write a poem" --provider claude
  ai "debug this code" --provider gemini --model gemini-pro
  ai chat --provider openai
        """
    )
    
    parser.add_argument("prompt", nargs="*", help="Your prompt (not needed for 'chat' command)")
    parser.add_argument("-p", "--provider", default="openai", 
                       choices=["openai", "claude", "gemini"],
                       help="AI provider to use")
    parser.add_argument("-m", "--model", help="Specific model to use")
    parser.add_argument("-s", "--stream", action="store_true", 
                       help="Stream response (if supported)")
    parser.add_argument("--history", action="store_true",
                       help="Use conversation history")
    
    args = parser.parse_args()
    
    ai = AIChat()
    
    # Interactive mode wenn "chat" als erstes Wort
    if args.prompt and args.prompt[0] == "chat":
        ai.interactive_mode(args.provider)
    elif args.prompt:
        prompt = " ".join(args.prompt)
        response = ai.chat(prompt, args.provider, args.model, args.stream, args.history)
        print(response)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
