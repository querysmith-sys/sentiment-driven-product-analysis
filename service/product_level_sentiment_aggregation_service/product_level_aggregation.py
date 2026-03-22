from service.sentiment_classification_service import sentiment_classifier as sc

dataset = sc.dataset

# group by product
sentiment_summary = (
    dataset.groupby("product_name")["sentiment"]
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
# print(sentiment_summary)
# print(type(sentiment_summary))
# print(sentiment_summary.head())