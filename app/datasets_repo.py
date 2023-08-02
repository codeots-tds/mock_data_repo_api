import pandas as pd
import os
from .util import *

class Data_Repository:
    def __init__(self, **kwargs):
        self.data_directory_path = kwargs.get('data_directory_path')
        try:
            self.list_of_datasets = os.listdir(self.data_directory_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Directory can't be found: {self.data_directory_path}")
        self.selected_dataset = None

    def filter_identifier_files(self):
        self.list_of_datasets = [file for file in self.list_of_datasets if not file.endswith('.Identifier')]

    def filter_non_csv(self):
        self.list_of_datasets = [file for file in self.list_of_datasets if is_csv(f'{self.data_directory_path}/{file}')]


data_files_path = '/home/ra-terminal/datasets/mock_api_data/'
data_repo = Data_Repository(data_directory_path=data_files_path)
data_repo.filter_identifier_files()
# print(data_repo.list_of_datasets)

if __name__ == '__main__':
    data_files_path = '/home/ra-terminal/datasets/mock_api_data/'
    data_repo = Data_Repository(data_directory_path=data_files_path)
    data_repo.filter_identifier_files()