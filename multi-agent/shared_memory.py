import sqlite3
import threading
import time
from typing import Optional, Dict, Any

class SharedMemory:
    """
    Simple shared memory store backed by SQLite.
    Thread-safe.
    """

    _lock = threading.Lock()

    def __init__(self, db_path=":memory:"):
        self.db_path = db_path
        self._conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self._create_tables()

    def _create_tables(self):
        with self._lock, self._conn:
            self._conn.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                type TEXT,
                timestamp REAL,
                info TEXT,
                thread_id TEXT
            )""")
            self._conn.execute("""
            CREATE TABLE IF NOT EXISTS extracted_values (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                thread_id TEXT,
                key TEXT,
                value TEXT,
                timestamp REAL
            )""")

    def log(self, source: str, type_: str, info: str, thread_id: Optional[str]=None):
        with self._lock, self._conn:
            timestamp = time.time()
            self._conn.execute(
                "INSERT INTO logs (source, type, timestamp, info, thread_id) VALUES (?, ?, ?, ?, ?)",
                (source, type_, timestamp, info, thread_id)
            )

    def save_extracted(self, thread_id: str, key: str, value: str):
        with self._lock, self._conn:
            timestamp = time.time()
            self._conn.execute(
                "INSERT INTO extracted_values (thread_id, key, value, timestamp) VALUES (?, ?, ?, ?)",
                (thread_id, key, value, timestamp)
            )
    
    def get_thread_logs(self, thread_id: str):
        with self._lock, self._conn:
            cursor = self._conn.execute(
                "SELECT * FROM logs WHERE thread_id = ? ORDER BY timestamp ASC",
                (thread_id,)
            )
            return [dict(row) for row in cursor.fetchall()]
    
    def get_extracted_values(self, thread_id: str):
        with self._lock, self._conn:
            cursor = self._conn.execute(
                "SELECT key, value FROM extracted_values WHERE thread_id = ? ORDER BY timestamp ASC",
                (thread_id,)
            )
            return {row["key"]: row["value"] for row in cursor.fetchall()}

