import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'data_repo.db')

drop_dogbite_table = """DROP TABLE IF EXISTS dogbite_table"""
create_dogbite_table = """CREATE TABLE IF NOT EXISTS dogbite_table(
                unique_id INTEGER PRIMARY KEY,
                date VARCHAR,
                species VARCHAR, 
                breed VARCHAR,
                age VARCHAR,
                gender VARCHAR,
                spayneuter VARCHAR,
                borough VARCHAR,
                zipcode INTEGER,
                year INTEGER
            );"""


drop_res_inspection_table = """DROP TABLE IF EXISTS rest_inspection_table"""
create_res_inspection_table = """
    CREATE TABLE IF NOT EXISTS rest_inspection_table(
        unique_id INTEGER PRIMARY KEY,
        camis INTEGER,	
        dba VARCHAR(50),	
        boro VARCHAR(20),
        building VARCHAR(30),
        street	VARCHAR(50),
        zipcode	INTEGER,
        phone	INTEGER,
        cuisine_description VARCHAR(50),	
        inspection_date VARCHAR(50),
        action	VARCHAR(50),
        violation_code	VARCHAR(50),
        violation_description VARCHAR(200),
        critical_flag	VARCHAR(50),
        score INTEGER,
        grade VARCHAR(5),
        grade_date	VARCHAR(50),
        record_date	VARCHAR(50),
        inspection_type	VARCHAR(100),
        latitude FLOAT,
        longitude FLOAT,
        community_board INTEGER,
        council_district INTEGER,
        census_tract INTEGER,
        bin INTEGER,
        bbl INTEGER,
        nta VARCHAR(30)
    );
"""
# Make the list a top-level variable
db_table_names = ['dogbite_table', 'rest_inspection_table']
create_table_queries = [create_dogbite_table, create_res_inspection_table]
drop_table_queries = [drop_dogbite_table, drop_res_inspection_table]