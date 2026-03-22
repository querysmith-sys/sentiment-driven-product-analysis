# type:ignore
import re
from nltk.corpus import stopwords
from service.upload_service import file_dataset as tf



dataset = tf.file_dataset
# print(dataset.columns)

# replace missing falue with null
dataset = dataset.dropna(subset=["Review"])
stop_words = set(stopwords.words("english"))

stop_words.remove("not")
stop_words.remove("no")

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^\w\s]", "", text)
    words = text.split()
    word = [word for word in words if word not in stop_words]
    return " ".join(word)

# print(clean_text("The battery is no bad and the phone is slow!"))
dataset["cleaned_review"] = dataset["Review"].apply(clean_text)
# print(dataset["cleaned_review"].head())