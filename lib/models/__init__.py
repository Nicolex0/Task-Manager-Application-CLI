import sqlite3

DATABASE_URL = "sqlite:///./task_manager.db"
CONN = sqlite3.connect(DATABASE_URL)
CURSOR = CONN.cursor()
