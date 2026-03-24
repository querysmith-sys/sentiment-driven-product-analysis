#type:ignore
import streamlit as st
import plotly.express as px


def sentiment_distribution_chart(dataset):

    sentiment_counts = dataset["sentiment"].value_counts().reset_index()
    sentiment_counts.columns = ["Sentiment", "Count"]

    fig = px.pie(
        sentiment_counts,
        values="Count",
        names="Sentiment",
        title="Sentiment Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)


def top_risky_products_chart(sentiment_summary, product_column):

    top_risk_products = sentiment_summary.sort_values(
        by="negative_percent",
        ascending=False
    ).head(10)

    fig = px.bar(
        top_risk_products,
        x="negative_percent",
        y=product_column,
        orientation="h",
        title="Top Risky Products"
    )

    st.plotly_chart(fig, use_container_width=True)