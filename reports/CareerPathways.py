# explore_skills.py
import streamlit as st
import sqlite3
import os

# Connect to SQLite Database
def connect_db():
    conn = sqlite3.connect('explore_skills.db')
    return conn

# Create the 'explore_skills' table and insert sample data if it doesn't exist
def create_explore_skills_table():
    conn = connect_db()
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS explore_skills (
                        skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        skill_name TEXT NOT NULL,
                        category TEXT NOT NULL,
                        level TEXT NOT NULL,
                        popularity INTEGER NOT NULL,
                        prerequisites TEXT)''')

    # Insert sample data if the table is empty
    cursor.execute("SELECT COUNT(*) FROM explore_skills")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''INSERT INTO explore_skills (skill_name, category, level, popularity, prerequisites)
                              VALUES (?, ?, ?, ?, ?)''', [
            ('Python Programming', 'Programming', 'Beginner', 1500, 'Basic computer knowledge'),
            ('Data Analysis', 'Programming', 'Intermediate', 1000, 'Python Programming'),
            ('Machine Learning', 'Programming', 'Advanced', 800, 'Data Analysis, Python Programming'),
            ('UI/UX Design', 'Design', 'Beginner', 1200, 'Basic design principles'),
            ('Graphic Design', 'Design', 'Intermediate', 900, 'UI/UX Design'),
            ('SEO Optimization', 'Marketing', 'Intermediate', 700, 'Content Writing, Digital Marketing'),
            ('Web Development', 'Programming', 'Beginner', 1800, 'Basic HTML and CSS'),
            ('Cloud Computing', 'IT', 'Advanced', 600, 'Networking, Linux basics'),
            ('Cybersecurity', 'IT', 'Advanced', 500, 'Networking, Cloud Computing'),
            ('Digital Illustration', 'Design', 'Beginner', 1000, 'Basic drawing skills'),
            ('Public Speaking', 'Communication', 'Beginner', 1400, None),
            ('Creative Writing', 'Writing', 'Intermediate', 1100, 'Basic writing skills'),
            ('Project Management', 'Management', 'Intermediate', 900, 'Team leadership experience'),
            ('DevOps', 'IT', 'Advanced', 400, 'Cloud Computing, Linux, Scripting')
        ])
        conn.commit()

    conn.close()

# Get skills data from the database
def get_skills(category=None, level=None):
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT skill_name, category, level, popularity, prerequisites FROM explore_skills WHERE 1=1"
    params = []

    if category:
        query += " AND category = ?"
        params.append(category)

    if level:
        query += " AND level = ?"
        params.append(level)

    cursor.execute(query, params)
    skills = cursor.fetchall()
    conn.close()
    return skills

# Display the Explore Skills interface
def display_explore_skills():
    st.title("Explore Skills")
    st.write("Browse and discover new skills based on categories and difficulty levels!")

    # Create table and insert data if needed
    create_explore_skills_table()

    # Dropdowns for filtering by category and level
    categories = ["All", "Programming", "Design", "Marketing", "IT", "Communication", "Writing", "Management"]
    levels = ["All", "Beginner", "Intermediate", "Advanced"]

    selected_category = st.selectbox("Select Category", categories)
    selected_level = st.selectbox("Select Skill Level", levels)

    # Fetch skills based on selected filters
    category_filter = None if selected_category == "All" else selected_category
    level_filter = None if selected_level == "All" else selected_level

    skills = get_skills(category_filter, level_filter)

    # Display the skills
    st.subheader(f"Skills in {selected_category if category_filter else 'All Categories'} ({selected_level if level_filter else 'All Levels'})")
    for skill_name, category, level, popularity, prerequisites in skills:
        st.write(f"**Skill**: {skill_name}")
        st.write(f"**Category**: {category}")
        st.write(f"**Level**: {level}")
        st.write(f"**Popularity**: {popularity}")
        if prerequisites:
            st.write(f"**Prerequisites**: {prerequisites}")
        st.write("---")


display_explore_skills()
