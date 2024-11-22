import streamlit as st
from textblob import TextBlob

st.title("Basic Sentiment Analysis")

st.write("Enter text below to analyze its sentiment:")

user_input = st.text_area("Your Text", "Type here...")

if st.button("Analyze"):
    if user_input.strip():
        analysis = TextBlob(user_input)
        sentiment = analysis.sentiment.polarity

        if sentiment > 0:
            st.success("Sentiment: Positive 😊")
        elif sentiment < 0:
            st.error("Sentiment: Negative 😢")
        else:
            st.info("Sentiment: Neutral 😐")
    else:
        st.warning("Please enter valid text!")
