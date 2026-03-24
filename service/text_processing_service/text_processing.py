# type:ignore
import re
from nltk.corpus import stopwords
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
    
def text_process(processed_dataset, review_column):
    
    # remove rows where review is missing
    dataset = processed_dataset.dropna(subset=[review_column]).copy()

    stop_words = set(stopwords.words("english"))
    # print(stop_words)

    stop_words.discard("not")
    stop_words.discard("no")

    def clean_text(text):
        text = str(text).lower()
        text = re.sub(r"[^\w\s]", " ", text).strip()

        words = text.split()
        filtered_words = [word for word in words if word not in stop_words]

        return " ".join(filtered_words)

    dataset["cleaned_review"] = dataset[review_column].apply(clean_text)

    return dataset
    
