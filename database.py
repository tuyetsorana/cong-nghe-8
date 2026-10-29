import sqlite3
import os
from datetime import datetime, date

DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "congnghe8_progress.db")

def get_connection():
    return sqlite3.connect(DB_NAME, timeout=20.0, check_same_thread=False)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL,
        student_class TEXT NOT NULL,
        lesson_id TEXT NOT NULL,
        score REAL NOT NULL,
        total_questions INTEGER NOT NULL,
        time_spent_sec INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_activity (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL,
        last_date TEXT NOT NULL,
        streak_days INTEGER DEFAULT 1
    )
    """)
    conn.commit()
    conn.close()

def save_result(student_name, student_class, lesson_id, score, total_questions, time_spent_sec):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO student_results (student_name, student_class, lesson_id, score, total_questions, time_spent_sec)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (student_name.strip(), student_class.strip(), lesson_id, score, total_questions, time_spent_sec))
    
    # Update streak
    today_str = date.today().isoformat()
    cursor.execute("SELECT id, last_date, streak_days FROM user_activity WHERE student_name = ?", (student_name.strip(),))
    row = cursor.fetchone()
    if row:
        user_id, last_date, streak = row
        if last_date != today_str:
            cursor.execute("UPDATE user_activity SET last_date = ?, streak_days = streak_days + 1 WHERE id = ?", (today_str, user_id))
    else:
        cursor.execute("INSERT INTO user_activity (student_name, last_date, streak_days) VALUES (?, ?, 1)", (student_name.strip(), today_str))
        
    conn.commit()
    conn.close()

def get_student_streak(student_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT streak_days FROM user_activity WHERE student_name = ?", (student_name.strip(),))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else 1

def get_leaderboard(lesson_id=None, limit=5):
    conn = get_connection()
    cursor = conn.cursor()
    if lesson_id:
        cursor.execute("""
        SELECT student_name, student_class, score, time_spent_sec, created_at
        FROM student_results
        WHERE lesson_id = ?
        ORDER BY score DESC, time_spent_sec ASC
        LIMIT ?
        """, (lesson_id, limit))
    else:
        cursor.execute("""
        SELECT student_name, student_class, score, time_spent_sec, created_at
        FROM student_results
        ORDER BY score DESC, time_spent_sec ASC
        LIMIT ?
        """, (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows
