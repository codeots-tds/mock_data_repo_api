import pandas as pd
import os


class Select_Dataset:
    def __init__(self, **kwargs):
          pass

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