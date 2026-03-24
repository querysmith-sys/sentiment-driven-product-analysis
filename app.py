# type:ignore
import streamlit as st
from service.upload_service.upload_service import process_dataset
from service.text_processing_service.text_processing import text_process
from service.sentiment_classification_service.sentiment_classifier import senti_classifier
from service.product_level_sentiment_aggregation_service.product_level_aggregation import product_based_senti_summary
from service.product_risk_identification_service.risk_calculation import risk_calc_summary
from service.visualization_service.visual import sentiment_distribution_chart, top_risky_products_chart


import nltk

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('sentiment/vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')


st.title("Product Review Sentiment Analyzer")

uploaded_file = st.file_uploader("Upload CSV")

product_column = st.text_input("Product Column Name")
review_column = st.text_input("Review Column Name")

run_analysis = st.button("Run Analysis")

if uploaded_file and run_analysis:
#  upload dataset to get dataframed dataset
    processed_dataset = process_dataset(
        uploaded_file
    )
    # text-processing 
    text_processed_dataset = text_process(processed_dataset,review_column)
    # sentiment classification
    sentiment_classified_data = senti_classifier(text_processed_dataset)
    # product-level-aggregation
    product_level_agg_dataset = product_based_senti_summary(sentiment_classified_data, product_column)
    # risk-identification
    risk_identified_dataset = risk_calc_summary(product_level_agg_dataset) 
    resulted_dataset = risk_identified_dataset.reset_index()
    st.success("Analysis completed")
    # visulaization
    sentiment_distribution_chart(sentiment_classified_data)
    top_risky_products_chart(resulted_dataset,product_column)
    # st.success("Analysis completed")
    st.dataframe(resulted_dataset)
    