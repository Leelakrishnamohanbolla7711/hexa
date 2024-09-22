import streamlit as st
import sqlite3

conn = sqlite3.connect('signup_data.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS signup_data
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT UNIQUE NOT NULL,
              email TEXT UNIQUE NOT NULL,
              password TEXT NOT NULL)''')

def signup():
    st.title("🔏 :red[Create An Account]")
    username = st.text_input("Username:red[*]",placeholder="Enter your username")
    email = st.text_input("Email:red[*]",placeholder="Enter your email")
    password = st.text_input("Password:red[*]", type="password",placeholder="Enter your password")

    signup_button = st.button(":red[Signup]")

    if signup_button:
    # Validate input (add more checks as needed)
        if not username or not email or not password:
            st.error("Please fill in all fields.")
        else:
            try:
                # Insert data into the database
                c.execute("INSERT INTO signup_data (username, email, password) VALUES (?, ?, ?)", (username, email, password))
                conn.commit()
                # Redirect to success page
                st.success("Signup successful!")
                st.session_state['show_signup'] = False
                st.rerun()
            except sqlite3.IntegrityError:
                st.error("Username or email already exists.")
    st.write("Already have an account?")
    if st.button("Login"):
        st.session_state['show_signup'] = False
        st.rerun()
    conn.close()

def login():
    st.title("🔐 Login to :green[Skill] Navigator")
    username = st.text_input("Username:red[*]",placeholder="Enter your username")
    password = st.text_input("Password:red[*]", type="password",placeholder="Enter your password")

    login_button = st.button(":green[Login]")
    if login_button:
            # Validate input
        if not username or not password:
            st.error("Please fill in all fields.")
        else:
        # Fetch data from the database
            c.execute("SELECT * FROM signup_data WHERE username=? AND password=?", (username, password))
            result = c.fetchone()

            if result:
                # Successful login
                st.success("Login successful!")
                # Redirect to a dashboard or other page (optional)
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Invalid username or password.")
    
    st.write("Don't have an account?")
    if st.button("signup"):
        st.session_state['show_signup'] = True
        st.rerun()

def logout():
    st.write("If you want to Logout click the Log out Button Below")
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

signup_page = st.Page(signup, title="Sign Up", icon=":material/login:")
login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon="🔓")

dashboard = st.Page("reports/ExploreSkills.py", title="Explore Skills", icon="🧭",default=True)
skills = st.Page("reports/SkillsDiscovery.py", title="Discover Skills", icon="🔍")
progress = st.Page(
    "reports/ProgressTracking.py", title="Progress", icon="📊"
)
careers = st.Page("reports/CareerPathways.py", title="Explore Careers", icon="🌐")
recomends = st.Page(
    "reports/PersonalizedRecomendations.py", title="Recomendations", icon="🎯"
)

search = st.Page("tools/ChatBot.py", title="ChatBot", icon="🤖")
history = st.Page("tools/History.py", title="History", icon="📜")

# Main Application Logic
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'show_signup' not in st.session_state:
    st.session_state['show_signup'] = False

if st.session_state['logged_in']:
    pg = st.navigation(

        {
            "Account": [logout_page],
            "Reports": [dashboard,skills,progress,careers,recomends],
            "Tools": [search, history],
        }
    )
else:
    if st.session_state['show_signup']:
        pg = st.navigation([signup_page])
    else:
        pg = st.navigation([login_page])
pg.run()