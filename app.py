import streamlit as st #type:ignore

st.title("Product Review Sentiment Analyzer")

uploaded_file = st.file_uploader("Upload CSV dataset")

if uploaded_file:
    st.success("File uploaded successfully")