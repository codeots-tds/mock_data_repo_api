from .schema import *
import sqlite3
import os

DIR = os.path.dirname(__file__)
DB_NAME = '/home/ra-terminal/Desktop/work/nycdohmh/projects/dataset_repo_api/data_db/data_repo.db'
DBPATH = os.path.join(DIR, DB_NAME)

# conn = sqlite3.connect('data_repo.db')
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

def run_schema(table_list):
    for table in table_list:
        cur.execute(table)
        print('creating table: ', table)
        print('done')

def save_data_to_db(df, table_name):
    try:
        # Write the data to a table
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"DataFrame is saved to database {DB_NAME} under table {table_name}.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    run_schema(create_table_queries)
    conn.commit()
    conn.close()
    pass