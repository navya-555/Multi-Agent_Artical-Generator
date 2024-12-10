import streamlit as st
from dotenv import load_dotenv
from crew_handler import execute_crew

# Load environment variables
load_dotenv()

# Streamlit configuration
st.set_page_config(
    page_title="Generate Articles",
    page_icon="assets/bot.png",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.header(":green[Generate Articles] 🤖")

# Input fields
topic = st.text_input("Enter the topic for the article")
col1, col2, col3 = st.columns([5, 5, 5])

with col1:
    no_words = st.text_input("No of words")
with col2:
    article_style = st.selectbox(
        "Article is for",
        ("Newspaper", "Commercial Magazine", "School Magazine", "Social Media", "Organization"),
    )
with col3:
    tone = st.selectbox("Tone should be", ("Formal", "Informal"))

# Generate button
if st.button("Generate"):
    if not topic or not no_words:
        st.error("Please fill in all fields before proceeding!")
    else:
        try:
            with st.spinner('Generating Response...'):
                # Call Crew logic
                result = execute_crew(topic, no_words, article_style, tone)
            st.markdown(result, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred: {e}")
