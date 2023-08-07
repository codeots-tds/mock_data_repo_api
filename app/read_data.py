import sys
sys.path.append("..")
import pandas as pd
import os
import sqlite3
# from data_db.seed import conn, cur

db_path = './data_db/data_repo.db'

class Read_Data:
    def __init__(self, db_conn):
        self.conn = db_conn
        self.cur = self.conn.cursor()
        self.query = "SELECT * FROM {}"
        self.selected_table = None
        self.years = None
        self.zipcodes_list = None
        pass
    
    def get_all_table_names(self):
        self.query_all_tables = "SELECT name FROM sqlite_master WHERE type='table';"
        self.cur.execute(self.query_all_tables)
        tables = self.cur.fetchall()
        tables = [x[0] for x in tables]
        return tables

    def select_table(self, tablename):
        self.selected_table = tablename
        tables = self.get_all_table_names()
        if self.selected_table in tables:
            print(f'{self.selected_table} exists in the database!')
            self.years = None
            self.zipcodes_list = None
            return self.selected_table
    
    def filter_by_year(self, year1, year2):
            if year2:
                self.years = f'''year BETWEEN {year1} AND {year2}'''
            else: 
                self.years = f'''year = {year1}'''

    def filter_by_zipcode(self, zipcodes = list):
        self.zipcodes_list = f"zipcode IN ({','.join(map(str, zipcodes))})"
    
    def build_query(self):
        if self.selected_table:
            query = "SELECT * FROM {}".format(self.selected_table)
            parameters = []
            if self.years:
                parameters.append(self.years)
            if self.zipcodes_list:
                parameters.append(self.zipcodes_list)
            if parameters: 
                query += ' WHERE ' + ' AND '.join(parameters)
            self.query = query
        else:
            print("No table selected.")


    def run_query(self):
        try:
            if self.query:
                print(f"Running SQL query: {self.query}", '<<<<<<<>>>>>>')
                self.cur.execute(self.query)
                rows = self.cur.fetchall()
                col_names = [desc[0] for desc in self.cur.description]
                df = pd.DataFrame(rows, columns=col_names)
                return df
            else:
                raise ValueError("No query to execute.")
        except Exception as e:
            print(f"An error occurred: {e}")

    

if __name__ == '__main__':
    # db_conn = sqlite3.connect(db_path)
    # read_data = Read_Data(db_conn)
    # print(read_data.get_all_table_names(), '-----------------------')
    # read_data.select_table('dogbite_table')
    # read_data.filter_by_year(2015, 2017)
    # read_data.filter_by_zipcode([11220, 11234, 11207])
    # read_data.build_query() 
    # df = read_data.run_query()
    # print(df.head(10))
    # read_data.conn.close()
    pass