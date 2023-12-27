import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load your NLP dataset (modify this with your data)
tw = pd.read_csv("ProjectTweets.csv", encoding = 'latin', header=None) 

tw = tw.rename(columns={0: 'number', 1: 'id_tweet', 2: 'date', 3: 'query', 4: 'user_id', 5: 'tweets'}) 


# Create a Streamlit app
st.title('NLP Dynamic Dashboard')

# Sidebar for user input
user_input = st.sidebar.text_input("Enter a keyword:")
selected_data = tw[tw['tweets'].str.contains(user_input, case=False)]

# Display the number of matching results
st.sidebar.write(f"Matching Results: {len(selected_data)}")

# Create a word cloud from the selected data
wordcloud = WordCloud(width=800, height=400).generate(' '.join(selected_data['tweets']))
st.image(wordcloud.to_array())

# Display the selected data in a table
st.write(selected_data)