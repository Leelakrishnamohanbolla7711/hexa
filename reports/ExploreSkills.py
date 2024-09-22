import streamlit as st
import time
from PIL import Image

# Main interface for Skill Navigator
def skill_navigator_page():
    # page_bg_img = """
    #             <style>
    #             [data-testid="stApp"]{
    #                     background-image: url();
    #                     background-size: cover;
    #                     }
    #             [data-testid="stHeader"]{
    #             background-color: rgba(0,0,0,0);
    #             }
    #             [data-testid="stSidebar"]{
    #             background-color: rgba(0,0,0,0);
    #             }
    #             </style>
    #             """

    # st.markdown(page_bg_img, unsafe_allow_html=True)
    # header_image = Image.open("header_image.jpg") 
    icon_image = Image.open("icon_image.png")  

   
    st.markdown(
        """
        <style>
        .main {
            background-image: url(https://www.pixelstalk.net/wp-content/uploads/images5/Free-Download-4K-White-Computer-Wallpaper-HD.jpg);
        }
        [data-testid="stHeader"]{
                background-color: rgba(0,0,0,0);
                }
                [data-testid="stSidebar"]{
                background-color: rgba(0,0,0,0);
                }
        .header-image {
            max-width: 100%;
            margin-bottom: 20px;
        }
        .title {
            font-family: 'Courier New', Courier, monospace;
            font-weight: bold;
            color: #007bff;
        }
        .section-title {
            color: #ff4500;
        }
        .info-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            color: #333333;
        }
        .main p, .main h1, .main h2, .main h3, .main h4, .main h5, .main h6 {
            color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display header image
    # st.image(header_image, use_column_width=True, caption="Navigate your skills with ease!", output_format="PNG")

    # Page title
    st.markdown("""<h1 style="color:black;">Welcome to Skill Navigator</h1>""",unsafe_allow_html=True)

    # Introduction section
    # st.header(f"Welcome, {st.session_state['username']}!")
    st.header(
        """
        Skill Navigator is your ultimate platform to explore, track, and develop new skills.
        Whether you are looking to upskill, reskill, or explore new career opportunities,
        Skill Navigator provides personalized recommendations and progress tracking.
        """
    )

    # Displaying icons with animations
    st.image(icon_image, width=150)
    st.markdown('<div class="section-title"><h3> 🚀 Features:</h3></div>', unsafe_allow_html=True)

    # Animated progress bar (simulating loading features)
    with st.spinner('Loading features...'):
        time.sleep(2)
    st.success('Features Loaded!')

    # Features section with info boxes
    st.markdown('<div class="info-box"><h4>🔍 Skill Discovery</h4><p>Explore new skills tailored to your interests and career goals.</p></div>', unsafe_allow_html=True)
    st.html("<p><a href='https://www.w3schools.com/'>W3Schools</a></p>")
    st.markdown('<div class="info-box"><h4>📊 Progress Tracking</h4><p>Monitor your progress and get personalized insights.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="info-box"><h4>🌐 Career Pathways</h4><p>Find out how to apply your skills in various industries and roles.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="info-box"><h4>🎯 Personalized Recommendations</h4><p>Receive skill-building recommendations based on your goals.</p></div>', unsafe_allow_html=True)

    return True

skill_navigator_page()