# JAXO — Personal AI Assistant

A beginner-friendly, modular desktop/terminal AI assistant project. This repository is being rebuilt as a learning project.

## What this first version includes
- Chat with an OpenAI-compatible API (OpenRouter supported).
- A simple terminal interface.
- Local conversation history in SQLite.
- Safe, allowlisted utility commands (time, date, calculator, help).
- Environment-based secret configuration.
- A modular structure that can grow into voice, desktop UI, tools, and automation.

> This is a starter, not a fully autonomous Jarvis. It does not execute arbitrary shell commands, control your computer, or run silently in the background.

## Requirements
- Python 3.10+
- An API key from OpenRouter or another OpenAI-compatible provider (optional for local utility commands).

## Setup (Linux / WSL)
```bash
git clone https://github.com/Ovho57/linux-.git
cd linux-
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set your key:
```env
OPENAI_API_KEY=your_key_here
OPENAI_BASE_URL=https://openrouter.ai/api/v1
AI_MODEL=deepseek/deepseek-chat
```

Keep your API key private. Never commit your real `.env` file.

## Run
```bash
python -m jaxo
```

## Commands
- `/help` — show commands
- `/time` — local time
- `/date` — local date
- `/calc 12 * (4 + 3)` — safe calculator
- `/history` — recent conversation
- `/clear` — clear the current chat context
- `/quit` — exit

## Project roadmap
1. Terminal assistant + API integration
2. Memory and settings
3. Voice input/output
4. Desktop GUI
5. Permission-based tools and plugins
6. Tests, packaging, and documentation

## Safety design
- No arbitrary shell execution from model output.
- No destructive actions without explicit confirmation.
- API keys are read from environment variables.
- Tool permissions should be narrow and auditable.

See [docs/ROADMAP.md](docs/ROADMAP.md) and [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).
