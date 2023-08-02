from flask import Flask, request, jsonify, Response, session, send_from_directory
from flask_cors import CORS
import pandas as pd
import numpy as np
import os

from read_data import read_data
from transform_data import Transform_Mock_Data
# from filter_data import Filter_Data

from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
CORS(app)
selected_dataset = None
app.secret_key = os.getenv('SECRET_KEY')  # Replace this with a real secret key!

download_file_path = '/home/ra-terminal/Desktop/work/nycdohmh/projects/mock_api/frontend_data_repo/static'
DB_PATH = ''

@app.route('/home/', methods =["GET"])
def get_all_files():
    return jsonify(read_data.get_all_table_names())

@app.route('/select_dataset', methods = ["POST"])
def select_dataset():
    global selected_dataset
    data = request.get_json()
    dataset_name = data.get('dataset_name')
    dataset_name = data.get('dataset_name')
    selected_dataset = read_data.select_table(dataset_name)
    
    return jsonify({"message" : "Dataset selected successfully", "dataset_name": dataset_name})


@app.route('/select_years', methods = ["POST"])
def select_years():
    data = request.get_json()
    years = list(data.get('years'))
    if len(years) == 2:
        read_data.filter_by_year(year1 = years[0], year2 = years[1])
    elif len(years) == 1:
        read_data.filter_by_year(year1 = years[0], year2 = None)
    return jsonify({"message" : "Years selected successfully", "years": years})

@app.route('/select_zipcodes', methods = ["POST"])
def select_zipcodes():
    data = request.get_json()
    zipcodes = data.get('zipcodes')
    read_data.filter_by_zipcode(zipcodes)
    filtered_data = read_data.run_query()
    return jsonify(filtered_data.to_dict(orient='records'))

@app.route('download_csv', methods=['GET'])
def download_data():
    filename = read_data.selected_table + ".csv"
    filtered_data = read_data.run_query()
    file_dir_path = '/home/ra-terminal/Desktop/work/nycdohmh/projects/dataset_repo_api/data_db/data_files'
    filtered_data.to_csv(f"{file_dir_path}/{filename}", index=False)
    return send_from_directory(directory=file_dir_path, filename=filename, as_attachment=True)