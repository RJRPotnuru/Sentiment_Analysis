import streamlit as st
from PIL import Image
st.title('Sentiment Analysis')
import joblib
clf=joblib.load('Sentiment Analysis')
ip=st.text_input('Enter your text')
op=clf.predict([ip])
if st.button('Predict'):
  st.title(op[0])
  if op[0]=='positive':
    image=Image.open('happy.jpeg')
    st.image(image,width=250)
  if op[0]=='negative': 
    image=Image.open('sad.jpeg')
    st.image(image,width=250)
