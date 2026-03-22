from service.product_level_sentiment_aggregation_service import product_level_aggregation as pla

sentiment_summary = pla.sentiment_summary

def classify_risk(neg_per):
    if neg_per > 50:
        return "High risk"
    elif neg_per >25:
        return "Medium risk"
    else:
        return "Low risk"

sentiment_summary["Risk"] = sentiment_summary["negative_percent"].apply(classify_risk)
print(sentiment_summary.sample())