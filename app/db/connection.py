import sqlite3
from contextlib import contextmanager

DATABASE_NAME = "bdo-job-management.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    try:
        yield conn
    finally:
        conn.close()