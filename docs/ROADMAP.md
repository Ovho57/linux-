# JAXO Development Roadmap

## Phase 1 — Working terminal assistant
- [x] Modular Python project layout
- [x] OpenAI-compatible API / OpenRouter client
- [x] SQLite conversation history
- [x] Safe local utilities: time, date, calculator
- [ ] Add automated tests

## Phase 2 — Better memory and settings
- User preferences stored separately from chat history
- Export and delete memory controls
- Config validation and model selection

## Phase 3 — Voice
- Push-to-talk microphone input
- Speech-to-text provider abstraction
- Text-to-speech provider abstraction
- Always show when microphone is active

## Phase 4 — Desktop UI
- Chat window, settings, microphone button, tool approval dialogs
- Accessible keyboard navigation

## Phase 5 — Tools and automation
- Read-only tools first
- Explicit allowlists and permissions
- Confirm before file writes, sending messages, or changing settings
- Audit log and disable-all-tools switch

## Phase 6 — Packaging
- Linux/Windows setup guides
- CI tests and release packaging
