"""LLM client. The model is not allowed to run system commands."""
from openai import OpenAI
from jaxo.config import settings

SYSTEM_PROMPT = """You are JAXO, a helpful personal assistant. Be clear and practical.
You may explain actions or suggest commands, but you cannot execute shell commands.
Never ask the user to reveal API keys, passwords, or private credentials."""

class Assistant:
    def __init__(self):
        self.client = None
        if settings.api_key:
            self.client = OpenAI(api_key=settings.api_key, base_url=settings.base_url)

    def reply(self, messages):
        if not self.client:
            return ("AI chat is not configured yet. Add OPENAI_API_KEY to your .env file. "
                    "Built-in commands such as /time and /calc still work.")
        response = self.client.chat.completions.create(
            model=settings.model,
            messages=[{"role": "system", "content": SYSTEM_PROMPT}, *messages],
            temperature=0.7,
        )
        return response.choices[0].message.content or "(No response)"
