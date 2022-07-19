import streamlit as st 
import joblib 

#load the joblib model 
model_nb = joblib.load('Tweets.csv')

#user input 
st.title("TWITTER AIRLINE SENTIMENT CLASSIFIER")
ip = st.text_input("Enter your message:")

#predict if the entered message is negative, positive or neutral 
op = model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])  #prints the output as negative, positive or neutral
