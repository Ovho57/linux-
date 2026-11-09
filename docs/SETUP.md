# Setup guide

1. Install Python 3.10 or newer.
2. Clone the repo and enter its folder.
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and add your provider key.
6. Run: `python -m jaxo`

If you only want to test the built-in commands, leave the API key blank and use `/time`, `/date`, and `/calc`.
