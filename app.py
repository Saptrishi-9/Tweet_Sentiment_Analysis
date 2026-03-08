import streamlit as st
from predict import predict_sentiment

# App Title
st.title("Tweet Sentiment Analysis")

st.write("Enter a tweet and the model will predict its sentiment.")

# Input box
tweet = st.text_area("Enter Tweet")

# Button
if st.button("Predict Sentiment"):

    if tweet.strip() == "":
        st.warning("Please enter a tweet.")
    else:

        result = predict_sentiment(tweet)

        # Positive
        if result == "Positive":
            st.markdown(
                f"""
                <div style="background-color:#28a745;
                            padding:15px;
                            border-radius:10px;
                            color:white;
                            font-size:20px;
                            text-align:center;">
                Sentiment: {result}
                </div>
                """,
                unsafe_allow_html=True
            )

        # Negative
        elif result == "Negative":
            st.markdown(
                f"""
                <div style="background-color:#dc3545;
                            padding:15px;
                            border-radius:10px;
                            color:white;
                            font-size:20px;
                            text-align:center;">
                Sentiment: {result}
                </div>
                """,
                unsafe_allow_html=True
            )

        # Neutral
        elif result == "Neutral":
            st.markdown(
                f"""
                <div style="background-color:#6c757d;
                            padding:15px;
                            border-radius:10px;
                            color:white;
                            font-size:20px;
                            text-align:center;">
                Sentiment: {result}
                </div>
                """,
                unsafe_allow_html=True
            )

        # Irrelevant
        else:
            st.markdown(
                f"""
                <div style="background-color:#adb5bd;
                            padding:15px;
                            border-radius:10px;
                            color:black;
                            font-size:20px;
                            text-align:center;">
                Sentiment: {result}
                </div>
                """,
                unsafe_allow_html=True
            )