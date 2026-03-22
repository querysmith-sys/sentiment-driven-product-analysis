from service.text_processing_service import text_processing as tp
from nltk.sentiment import SentimentIntensityAnalyzer # type: ignore
# print(tp.clean_text("phone not good!"))

sia = SentimentIntensityAnalyzer()
# print(sia)

# generatin compund score

dataset = tp.dataset
dataset["compound"] = dataset["cleaned_review"].apply(lambda review: sia.polarity_scores(review)["compound"])
# data = sia.polarity_scores("bad")["compound"]
# print(data)
# print(dataset["compound"])

# infering sentiment from compund score us e VADER rules

def infer_sentiment(score):
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"

dataset["sentiment"] = dataset["compound"].apply(infer_sentiment)

# print(dataset[["product_name", "cleaned_review", "sentiment", "compound"]].head())