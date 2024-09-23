# skill_discovery.py
import streamlit as st
import sqlite3
#st.write("Hello")

# # Connect to SQLite Database
def connect_db():
    
    conn = sqlite3.connect('skills.db')
    # c=conn.cursor()
    
    return conn
# def create_table():
#     c=connect_db()
#     cursor=c.cursor()
#     c.execute("CREATE TABLE IF NOT EXISTS  skills (skill_id INTEGER PRIMARY KEY, skill_name TEXT, category TEXT)")
    
def create_skill_table():
    conn = connect_db()
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS skills (
                        skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        skill_name TEXT NOT NULL,
                        category TEXT NOT NULL)''')

    # Insert sample data if the table is empty
    cursor.execute("SELECT COUNT(*) FROM skills")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''INSERT INTO skills (skill_name, category)
                              VALUES (?, ?)''', [
            ('Python Programming', 'Programming'),
            ('Data Analysis', 'Programming'),
            ('Machine Learning', 'Programming'),
            ('UI/UX Design', 'Design'),
            ('Graphic Design', 'Design'),
            ('Social Media Marketing', 'Marketing'),
            ('SEO Optimization', 'Marketing'),
            ('Content Writing', 'Writing'),
            ('Copywriting', 'Writing'),
            ('Web Development', 'Programming'),
            ('App Development', 'Programming'),
            ('Digital Illustration', 'Design'),
            ('Brand Strategy', 'Marketing'),
            ('Product Management', 'Management'),
            ('Project Management', 'Management'),
            ('Public Speaking', 'Communication'),
            ('Creative Writing', 'Writing'),
            ('Cloud Computing', 'IT'),
            ('DevOps', 'IT'),
            ('Cybersecurity', 'IT')
        ])
        conn.commit()

    conn.close()

def get_skills():
    c=connect_db()
    cursor = c.cursor()
    cursor.execute("SELECT skill_name, category FROM skills")
    skills = cursor.fetchall()
    c.close()
    return skills

def display_skill_discovery():
    create_skill_table()
    st.title("Skill Discovery")
    st.write("Discover new skills based on your interests!")
    
    skills = get_skills()
    
    categories = sorted(set([skill[1] for skill in skills]))
    selected_category = st.selectbox("Select Category", categories)
    
    st.subheader(f"Skills in {selected_category}")
    for skill in skills:
        if skill[1] == selected_category:
            st.write(f"Skill: {skill[0]}")
    

display_skill_discovery()
