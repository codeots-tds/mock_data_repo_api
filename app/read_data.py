import pandas as pd
from datasets_repo import data_repo

class Read_Data:
    def __init__(self, **kwargs):
        self.selected_dataset = kwargs.get('selected_file')
        self.selected_df = pd.DataFrame()

    def read_data(self):
        self.selected_df = pd.read_csv(f'/home/ra-terminal/datasets/mock_api_data/{self.selected_dataset}')


selected_data = Read_Data(selected_file = data_repo.selected_dataset)
selected_data.read_data()