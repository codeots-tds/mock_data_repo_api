import pandas as pd
import os

def is_csv(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lower() == '.csv'

def read_data(dataset_path):
    if is_csv(dataset_path):
        dataset_df = pd.read_csv(dataset_path)
        return dataset_df