from datasets_repo import data_repo
import pandas as pd

class Transform_Mock_Data:
    def __init__(self, **kwargs):
        self.selected_dataset = kwargs.get('data')

    def parse_year(self):
        date_cols = ['dateofbite', 'inspection date', 'date_of_interest']
        for col in date_cols:
            if col in list(self.selected_dataset.columns):
                self.selected_dataset[col] = pd.to_datetime(self.selected_dataset[col])
                self.selected_dataset['year'] = self.selected_dataset[col].dt.year
        return self.selected_dataset
    
    def cols_to_lower(self):
        self.selected_dataset.columns = self.selected_dataset.columns.str.lower() 
        return self.selected_dataset
    
    def convert_col_types(self):
        cols_to_convert = ['year', 'zipcode']
        for col in cols_to_convert:
            if col in list(self.selected_dataset.columns):
                self.selected_dataset[col] = pd.to_numeric(self.selected_dataset[col], errors='coerce').fillna(0).astype(int)
        return self.selected_dataset


if __name__ == '__main':
    transformed_data = Transform_Mock_Data(data = data_repo.selected_data_df)
    transformed_data.parse_year()
    pass