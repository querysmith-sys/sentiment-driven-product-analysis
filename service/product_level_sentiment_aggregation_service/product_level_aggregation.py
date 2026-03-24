
def product_based_senti_summary(sentiment_classified_data, product_column):
    sentiment_summary = (
        sentiment_classified_data.groupby(product_column)["sentiment"]
        .value_counts()
        .unstack()
        .reindex(columns=["negative", "neutral", "positive"], fill_value=0)
        .fillna(0)
        .astype(int)
)
    sentiment_summary["total_reviews"] = (sentiment_summary["positive"] +
        sentiment_summary["negative"] +
        sentiment_summary["neutral"])
    sentiment_summary["negative_percent"] = (sentiment_summary["negative"]/sentiment_summary["total_reviews"])*100
    sentiment_summary["negative_percent"] = sentiment_summary["negative_percent"].round(2)
    sentiment_summary = sentiment_summary.sort_values(
    by="negative_percent",
    ascending=False
)
    return sentiment_summary
