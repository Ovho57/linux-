"""Small SQLite conversation-history store."""
import sqlite3
from pathlib import Path
from typing import Iterable

class Memory:
    def __init__(self, database: str):
        self.database = database
        with self._connect() as db:
            db.execute("""CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )""")

    def _connect(self):
        return sqlite3.connect(self.database)

    def add(self, role: str, content: str) -> None:
        with self._connect() as db:
            db.execute("INSERT INTO messages(role, content) VALUES (?, ?)", (role, content))

    def recent(self, limit: int = 12) -> list[tuple[str, str]]:
        with self._connect() as db:
            rows = db.execute(
                "SELECT role, content FROM messages ORDER BY id DESC LIMIT ?", (limit,)
            ).fetchall()
        return list(reversed(rows))

    def clear(self) -> None:
        with self._connect() as db:
            db.execute("DELETE FROM messages")
