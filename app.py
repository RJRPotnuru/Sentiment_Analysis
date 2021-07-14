import streamlit as st
from PIL import Image
import joblib
clf=joblib.load('Sentiment Analysis')
nav = st.sidebar.radio("Navigation",["Analyse the text","Overview",])

if nav == "Overview":
    st.title("Sentiment Analysis")
    st.write("Feedback is very important for any company or industry.They often want to know in time what consumers and the public  think of their products and services. However, it is not realistic to manually read every post on the website and extract useful viewpoint information from it.Sentiment analysis allows large-scale processing of data in an efficient manner. This project used a dataset of the Amazon reviews and then built a model to predict the sentiment of the comment given the comment declaration by using Python and machine learning algorithm- Naïve Bayes.")
    image = Image.open("image.png")
    st.image(image,width = 400)
if nav == "Analyse the text":
    st.title("Sentiment Analysis")
    st.subheader("Enter Text to analyse: ")
    text = st.text_input(" ")
    st.write("Note: For accurate Prediction, please enter minimum of 10-20 words as model is trained with such reviews.Please click Enter after typing the text and then proceed to click Predict button")
    op=clf.predict([text])
    if st.button('Predict'):
      st.title(op[0])
      if op[0]=='positive':
        image=Image.open('happy.jpeg')
        st.image(image,width=250)
      if op[0]=='negative': 
        image=Image.open('sad.jpeg')
        st.image(image,width=250)
