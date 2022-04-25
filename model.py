import streamlit as st 
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

st.write("# Real Time Sentiment Analysis")

user_input = st.text_input("Please rate our services >>: ")
nltk.download("vader_lexicon")

# performing sentiment analysis
s = SentimentIntensityAnalyzer()
score = s.polarity_scores(user_input)       # returns output in form of dict

if score == 0:
    st.write(" ")
elif score["neg"] !=0 :
    st.write("# Negative")
elif score["pos"] !=0:
    st.write("# Positive")