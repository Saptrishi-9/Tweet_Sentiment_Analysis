### Tweet Sentiment Analysis

This project is an end-to-end Natural Language Processing (NLP) application that predicts the sentiment of tweets using a deep learning model. The system processes raw tweet text, converts it into numerical representations using Word2Vec embeddings, and classifies the sentiment into four categories: Positive, Negative, Neutral, or Irrelevant. The trained model is integrated into an interactive web interface built using Streamlit, allowing users to input tweets and instantly receive sentiment predictions.

#### Workflow Overview

Dataset
    ↓
Cleaning
    ↓
Tokenization
    ↓
Lemmatization
    ↓
Word2Vec Embedding
    ↓
BiLSTM
    ↓
Evaluation
    ↓
Save Model
    ↓
Prediction Pipeline
    ↓
Deployment


#### Libraries used
Scikit-Learn, Gensim, Numpy, Nltk, Tensorflow, Keras, Streamlit