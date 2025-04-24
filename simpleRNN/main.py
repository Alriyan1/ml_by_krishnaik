import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import  imdb
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence


word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}


model=load_model('D:\ml_by_krishNaik\simpleRNN\simple_rnn_model.h5')

def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])

def preprocess_text(text):
    words= text.lower().split()
    encoded_raview = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_raview], maxlen=500)
    return padded_review

def predict_sentiment(review):
    preprocessed_input = preprocess_text(review)
    prediction = model.predict(preprocessed_input)
    sentiment = 'positive' if prediction[0][0] > 0.5 else 'negative'
    return sentiment, prediction[0][0]


import streamlit as st
st.title('IMBD Movie Review Sentiment Analysis')
st.write('Enter a movie review below:')

user_input = st.text_area("Movie Review", "Type Here")
if st.button('Predict'):
    preprocessd_input = preprocess_text(user_input)
    prediction = model.predict(preprocessd_input)
    sentiment = 'positive' if prediction[0][0] > 0.5 else 'negative'
    st.write(f"Sentiment: {sentiment}")
    st.write(f"Prediction Score: {prediction[0][0]}")
else:
    st.write("Enter a review and click 'Predict' to see the sentiment.")