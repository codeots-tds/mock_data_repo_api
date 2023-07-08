import pandas as pd


class Filter_Data:
    def __init__(self, **kwargs):
        self.selected_data = kwargs.get('selected_dataset')


    def filter_by_year(self, year1, year2):
        if year2 is not None:
            self.selected_data = self.selected_data[(self.selected_data['year'] >= year1) & (self.selected_data['year'] <= year2)]
        else: 
            self.selected_data = self.selected_data[(self.selected_data['year'] == year1)]
        return self.selected_data



if __name__ == '__main__':
    pass
