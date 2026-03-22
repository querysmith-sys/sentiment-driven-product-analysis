# later handle web interface for upload and receive od dataset from user using frameworks.
# here i am testing and starting with assumeing i have the dataset already.

import pandas as pd # type: ignore


def load_dataset():
    file = pd.read_csv('service/upload_service/Dataset-SA.csv')
    return file
file_dataset = pd.DataFrame(load_dataset())


