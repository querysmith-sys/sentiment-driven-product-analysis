# from service.product_level_sentiment_aggregation_service import product_level_aggregation as pla

# sentiment_summary = pla.sentiment_summary



def risk_calc_summary(product_level_agg_dataset):
    def classify_risk(neg_per):
        if neg_per > 50:
            return "High risk"
        elif neg_per >25:
            return "Medium risk"
        else:
            return "Low risk"
    product_level_agg_dataset["Risk"] = product_level_agg_dataset["negative_percent"].apply(classify_risk)
    return product_level_agg_dataset
