import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns([2, 3], gap = "medium")

with col1: 
    st.image(image = "C:/Users/60102/Desktop/NBA_Prediction_Site/IMG_5135.jpg")

with col2:
    st.title("About Me 🙋‍♂️")
    st.subheader("Hello! I am Ling Yang En and I am in my final semester studying computer science at the University of Wollongong Malaysia. This is a website about how I used Machine Learning to predict the 2023 NBA Championship Teams!")
