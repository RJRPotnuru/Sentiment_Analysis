import streamlit as st
st.title('Sentiment Analysis')
import joblib
clf=joblib.load('Sentiment Analysis')
ip=st.text_input('Enter your text')
op=clf.predict([ip])
if st.button('Predict'):
  st.title(op[0])
