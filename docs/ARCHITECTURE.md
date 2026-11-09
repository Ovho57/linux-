# Architecture

```text
User
  ↓
Terminal UI (jaxo/cli.py)
  ├── Built-in safe tools (jaxo/tools.py)
  ├── Local history (jaxo/memory.py → SQLite)
  └── AI provider client (jaxo/ai.py → OpenAI-compatible API)
                         ↓
                  Provider / model
```

## Design principles
- Keep UI, AI provider, memory, and tools in separate modules.
- Model responses are data, not executable instructions.
- Tools have narrow input/output contracts.
- Add permissions before introducing computer-control features.
- Never store secrets in source code or chat history.
