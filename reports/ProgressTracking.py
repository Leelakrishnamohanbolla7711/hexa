# progress_tracking.py
import streamlit as st
import sqlite3
import os
from datetime import date

# Connect to SQLite Database
def connect_db():
    conn = sqlite3.connect('progress.db')
    return conn

# Create the 'user_progress' table and insert sample data if it doesn't exist
def create_progress_table():
    conn = connect_db()
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_progress (
                        user_id INTEGER NOT NULL,
                        skill_name TEXT NOT NULL,
                        progress INTEGER NOT NULL,
                        last_updated DATE NOT NULL,
                        PRIMARY KEY (user_id, skill_name)
                    )''')

    # Insert sample data if the table is empty
    cursor.execute("SELECT COUNT(*) FROM user_progress")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''INSERT INTO user_progress (user_id, skill_name, progress, last_updated)
                              VALUES (?, ?, ?, ?)''', [
            (1, 'Python Programming', 80, '2024-09-23'),
            (1, 'Machine Learning', 50, '2024-09-20'),
            (1, 'UI/UX Design', 30, '2024-09-18'),
            (2, 'Data Analysis', 70, '2024-09-21'),
            (2, 'Cybersecurity', 40, '2024-09-15'),
            (3, 'Web Development', 90, '2024-09-22'),
            (3, 'Project Management', 60, '2024-09-19')
        ])
        conn.commit()

    conn.close()

# Get the user's progress from the database
def get_user_progress(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT skill_name, progress FROM user_progress WHERE user_id = ?", (user_id,))
    progress_data = cursor.fetchall()
    conn.close()
    return progress_data

# Display the Progress Tracking feature
def display_progress_tracking(user_id):
    st.title("Progress Tracking")
    st.write("Track your progress in different skills!")

    # Create table and insert sample data if needed
    create_progress_table()

    progress_data = get_user_progress(user_id)
    
    for skill, progress in progress_data:
        st.subheader(f"Skill: {skill}")
        st.progress(progress)

 # Placeholder for logged-in user ID
user_id = 1  # You can replace this with dynamic user ID based on login
display_progress_tracking(user_id)
