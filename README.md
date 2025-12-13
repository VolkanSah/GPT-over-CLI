
**Was drin ist:**
- 3 Provider (OpenAI, Claude, Gemini) - einfach erweiterbar
- Conversation History für Context
- Interactive Chat Mode
- Streaming-Support (Skeleton)
- Config System (noch dummy)

**Quick Setup:**
```bash
chmod +x ai.py
./ai.py "test prompt" --provider claude
./ai.py chat --provider openai  # interactive
```

**Was ich noch machen musst:**
1. Echte API-Calls in den Provider-Klassen
2. Config File Support (`~/.aichat.json` mit Keys)???
3. Streaming implementieren 

