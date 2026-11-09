"""Terminal interface for JAXO."""
from jaxo.ai import Assistant
from jaxo.config import settings
from jaxo.memory import Memory
from jaxo.tools import run_command

HELP = """Commands:
  /help          Show this help
  /time          Current local time
  /date          Current local date
  /calc EXPR     Safe arithmetic calculator
  /history       Show recent saved messages
  /clear         Clear saved chat
  /quit          Exit JAXO
"""

def main():
    assistant = Assistant()
    memory = Memory(settings.database)
    print("\nJAXO — Personal AI Assistant (starter)\nType /help for commands.\n")
    while True:
        try:
            user = input("You > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break
        if not user:
            continue
        if user in {"/quit", "/exit"}:
            print("Goodbye.")
            break
        if user == "/help":
            print(HELP)
            continue
        if user == "/history":
            for role, content in memory.recent():
                print(f"{role}: {content}")
            continue
        if user == "/clear":
            memory.clear()
            print("Conversation history cleared.")
            continue
        result = run_command(user)
        if result is not None:
            print(f"JAXO > {result}")
            continue
        memory.add("user", user)
        response = assistant.reply(memory.recent())
        memory.add("assistant", response)
        print(f"JAXO > {response}\n")
