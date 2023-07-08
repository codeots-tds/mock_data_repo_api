import pandas as pd
import os

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

    def select_datafile(self, filename):
        self.selected_dataset = next((file for file in self.list_of_datasets if file == filename), None)
        return self.selected_dataset
    
    def get_selected_datapath(self):
        if self.selected_dataset is not None:
            self.selected_data_filepath = os.path.join(self.data_directory_path, self.selected_dataset)
            return self.selected_data_filepath
        else:
            raise FileNotFoundError("No dataset has been selected.")

    def load_selected_datafile(self):
        selected_data_filepath = self.get_selected_datapath()
        if selected_data_filepath is not None:
            self.selected_data_df = pd.read_csv(selected_data_filepath)
            return self.selected_data_df
        else:
            raise FileNotFoundError("Cannot load data, no valid dataset file path found.")

data_files_path = '/home/ra-terminal/datasets/mock_api_data/'
data_repo = Data_Repository(data_directory_path=data_files_path)
data_repo.filter_identifier_files()

if __name__ == '__main__':
    data_files_path = '/home/ra-terminal/datasets/mock_api_data/'
    data_repo = Data_Repository(data_directory_path=data_files_path)
    data_repo.filter_identifier_files()