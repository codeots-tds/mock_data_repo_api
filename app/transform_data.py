import sys
sys.path.append("..")
# from datasets_repo import data_repo
from app.datasets_repo import data_repo
import pandas as pd
from .util import *
from data_db.seed import save_data_to_db
from data_db.schema import *

class Transform_Mock_Data:
    def __init__(self, **kwargs):
        # self.selected_dataset = kwargs.get('data')
        self.datasets = kwargs.get('lists_of_datasets')
        self.data_files_path = '/home/ra-terminal/datasets/mock_api_data/'

    def load_data_to_dict(self):
        self.datasets_dict = {}
        for dataset in self.datasets:
            if is_csv(f'{self.data_files_path}/{dataset}'):
                dataset_df = read_data(os.path.join(self.data_files_path, dataset))
                self.datasets_dict[dataset] = dataset_df

    def parse_year(self):
        date_cols = ['dateofbite', 'inspection date', 'date_of_interest']
        for dataset_name, dataset in self.datasets_dict.items():
            self.datasets_dict[dataset_name]['year'] = None
            for col in date_cols:
                if col in list(dataset.columns):
                    dataset[col] = pd.to_datetime(dataset[col])
                    self.datasets_dict[dataset_name]['year'] = dataset[col].dt.year

    def fill_0(self):
        for dataset_name, dataset in self.datasets_dict.items():
            self.datasets_dict[dataset_name]['year'] = dataset['year'].fillna(0)

    def cols_to_lower(self):
        for dataset_name, dataset in self.datasets_dict.items():
            self.datasets_dict[dataset_name].columns = dataset.columns.str.lower()
    
    def convert_col_types(self):
        cols_to_convert = ['year', 'zipcode']
        for dataset_name, dataset in self.datasets_dict.items():
            for col in cols_to_convert:
                if col in list(dataset):
                    dataset[col] = pd.to_numeric(dataset[col], errors='coerce').fillna(0).astype(int)
                    self.datasets_dict[dataset_name][col] = dataset[col]

transformed_data = Transform_Mock_Data(lists_of_datasets = data_repo.list_of_datasets)
transformed_data.load_data_to_dict()
transformed_data.cols_to_lower()
transformed_data.parse_year()
transformed_data.fill_0()
transformed_data.convert_col_types()

# for idx, (ds_name, dataset) in enumerate(transformed_data.datasets_dict.items()):
#     save_data_to_db(dataset, db_table_names[idx])
#     print(f'Finished loading {ds_name}')
#     print(idx, ds_name, dataset)

if __name__ == '__main__':
    # transformed_data = Transform_Mock_Data(lists_of_datasets = data_repo.list_of_datasets)
    # transformed_data.load_data_to_dict()
    # transformed_data.cols_to_lower()
    # transformed_data.parse_year()
    # transformed_data.fill_0()
    # transformed_data.convert_col_types()
    pass