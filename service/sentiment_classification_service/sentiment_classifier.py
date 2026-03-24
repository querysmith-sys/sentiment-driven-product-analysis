# from service.text_processing_service import text_processing as tp
from nltk.sentiment import SentimentIntensityAnalyzer # type: ignore
# print(tp.clean_text("phone not good!"))



# ensure lexicon exists
try:
    nltk.data.find('sentiment/vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')
    
sia = SentimentIntensityAnalyzer()
# print(sia)


def senti_classifier(text_processed_dataset):
    text_processed_dataset["compound"] = text_processed_dataset["cleaned_review"].apply(lambda review: sia.polarity_scores(review)["compound"])
    def infer_sentiment(score):
        if score >= 0.05:
            return "positive"
        elif score <= -0.05:
            return "negative"
        else:
            return "neutral"
    
    text_processed_dataset["sentiment"] = text_processed_dataset["compound"].apply(infer_sentiment)
    return text_processed_dataset