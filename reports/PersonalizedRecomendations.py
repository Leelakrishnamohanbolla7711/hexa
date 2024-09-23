# skill_recommendations.py
import streamlit as st
import sqlite3
import os
from datetime import date

# Connect to SQLite Database
def connect_db():
    conn = sqlite3.connect('skill_recommendations.db')
    return conn

# Create the 'user_skill_recommendations' table and insert sample data if it doesn't exist
def create_recommendations_table():
    conn = connect_db()
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_skill_recommendations (
                        recommendation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        skill_name TEXT NOT NULL,
                        recommendation_reason TEXT NOT NULL,
                        date_recommended DATE NOT NULL
                    )''')

    # Insert sample data if the table is empty
    cursor.execute("SELECT COUNT(*) FROM user_skill_recommendations")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''INSERT INTO user_skill_recommendations (user_id, skill_name, recommendation_reason, date_recommended)
                              VALUES (?, ?, ?, ?)''', [
            (1, 'Python Programming', 'Skill Gap - Required for Data Science', '2024-09-23'),
            (1, 'Data Analysis', 'Career Path - Data Scientist', '2024-09-24'),
            (2, 'SEO Optimization', 'Skill Gap - Boost marketing efforts', '2024-09-21'),
            (2, 'Content Writing', 'Career Path - Digital Marketer', '2024-09-22'),
            (3, 'Machine Learning', 'Skill Gap - Enhance AI knowledge', '2024-09-20'),
            (3, 'Cloud Computing', 'Career Path - Cloud Engineer', '2024-09-19')
        ])
        conn.commit()

    conn.close()

# Get recommendations for a user
def get_user_recommendations(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT skill_name, recommendation_reason, date_recommended FROM user_skill_recommendations WHERE user_id = ?", (user_id,))
    recommendations = cursor.fetchall()
    conn.close()
    return recommendations

# Display the Skill Recommendations feature
def display_skill_recommendations(user_id):
    st.title("Skill Recommendations")
    st.write("Here are some personalized skill recommendations for you!")

    # Create table and insert sample data if needed
    create_recommendations_table()

    recommendations = get_user_recommendations(user_id)

    if recommendations:
        for skill_name, reason, date_recommended in recommendations:
            st.subheader(f"Recommended Skill: {skill_name}")
            st.write(f"**Reason**: {reason}")
            st.write(f"**Date Recommended**: {date_recommended}")
            st.write("---")
    else:
        st.write("No recommendations found for this user.")


# Placeholder for logged-in user ID
user_id = 1  # You can replace this with dynamic user ID based on login
display_skill_recommendations(user_id)
