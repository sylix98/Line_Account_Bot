# db.py
import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('accounting.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            amount INTEGER,
            time TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_record(category, amount):
    conn = sqlite3.connect('accounting.db')
    c = conn.cursor()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO records (category, amount, time) VALUES (?, ?, ?)",
              (category, amount, now))
    conn.commit()
    conn.close()

def today_records():
    conn = sqlite3.connect('accounting.db')
    c = conn.cursor()
    today = datetime.now().strftime('%Y-%m-%d')
    c.execute("SELECT category, amount FROM records WHERE time LIKE ?", (today + '%',))
    result = c.fetchall()
    conn.close()
    return result
