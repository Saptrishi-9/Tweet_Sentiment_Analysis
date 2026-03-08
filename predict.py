# Importing Libraries
import numpy as np
from tensorflow.keras.models import load_model
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from gensim.models import Word2Vec

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')


# Load the Model
model = load_model('tweet_sentiment_analysis_model.h5')

# Load Word2Vec
w2v_model = Word2Vec.load('w2v_model.model')

lemmatizer = WordNetLemmatizer()


import re

def clean_tweet(text):
    text = str(text).strip()                    # remove leading/trailing whitespace
    text = re.sub(r'http\S+|www\S+', '', text)  # remove URLs
    text = re.sub(r'@\w+', '', text)            # remove mentions
    text = re.sub(r'#', '', text)               # remove hashtags symbol
    text = re.sub(r'[^a-zA-Z\s]', '', text)     # remove numbers, punctuation, special chars
    text = text.lower()
    
    tokens = word_tokenize(text)                # Tokenisation

    tokens = [lemmatizer.lemmatize(word) for word in tokens]  #Lemmetization

    return tokens


max_len = 65

vector_size = w2v_model.vector_size

def tweet_to_sequence(words):

    sequence = []

    for word in words:
        if word in w2v_model.wv:
            sequence.append(w2v_model.wv[word])
        else:
            sequence.append(np.zeros(vector_size))

    sequence = sequence[:max_len]

    while len(sequence) < max_len:
        sequence.append(np.zeros(vector_size))

    return np.array(sequence)

sentiment_map = {
    0: "Irrelevant",
    1: "Negative",
    2: "Neutral",
    3: "Positive"
}


def predict_sentiment(tweet):

    tokens = clean_tweet(tweet)                     # Preprocessing tweet

    sequence = tweet_to_sequence(tokens)            # Converting to Word2Vec sequence

    sequence = np.expand_dims(sequence,axis=0)      # Reshaping for the model

    prediction = model.predict(sequence)

    label = np.argmax(prediction)

    return sentiment_map[label]
