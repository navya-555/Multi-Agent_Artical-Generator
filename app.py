import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


st.set_page_config(page_title="Generate Articles",
                    page_icon='bot.png',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header(":green[Generate Articles] 🤖")

input_text=st.text_input("Enter the topic for article")

col1,col2,col3=st.columns([5,5,5])

with col1:
    no_words=st.text_input('No of words')
with col2:
    article_style=st.selectbox('Article is for',('Newspaper','Commercial Magazine','School Magazine','Social Media','Organization'))
with col3:
    tone=st.selectbox('Tone should be',('Formal','Informal'))

submit=st.button("Generate")


