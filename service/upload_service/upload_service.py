# later handle web interface for upload and receive od dataset from user using frameworks.
# here i am testing and starting with assumeing i have the dataset already.

import pandas as pd # type: ignore


def process_dataset(dataset):

    dataset = pd.read_csv(dataset)
    newDataset = pd.DataFrame(dataset)
    return dataset


# file_dataset = upload_service()


