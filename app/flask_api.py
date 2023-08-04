from flask import Flask, request, jsonify, send_from_directory, g
from flask_cors import CORS

from .read_data import Read_Data, db_path

from dotenv import load_dotenv
import json
import sqlite3
from redis import Redis
load_dotenv()

app = Flask(__name__)
CORS(app)

# app.config['REDIS_HOST'] = 'localhost'
# app.config['REDIS_PORT'] = 6379
# redis = Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])

redis = Redis(host='localhost', port = 6379)

@app.before_request
def before_request():
    g.db = sqlite3.connect(db_path)
    g.dataset_download = Read_Data(g.db)

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


@app.route('/home', methods =["GET"])
def get_all_files():
    return jsonify(g.dataset_download.get_all_table_names())

@app.route('/select_dataset', methods = ["POST"])
def select_dataset():
    data = request.get_json()
    dataset_name = data.get('dataset_name')
    g.dataset_download.select_table(dataset_name)
    redis.set('selected_dataset', dataset_name)
    return jsonify({"message" : "Dataset selected successfully", "dataset_name": dataset_name})


@app.route('/select_years', methods = ["POST"])
def select_years():
    data = request.get_json()
    years = list(data.get('years'))
    redis.set('selected_years', json.dumps(years))
    return jsonify({"message" : "Years selected successfully", "years": years})

@app.route('/select_zipcodes', methods = ["POST"])
def select_zipcodes():
    data = request.get_json()
    zipcodes = data.get('zipcodes')
    redis.set('selected_zipcodes', json.dumps(zipcodes))
    # g.dataset_download.run_query()
    # return jsonify(dataset_download.to_dict(orient='records'))
    return jsonify({"message" : "Zipcodes selected successfully", "zipcodes": zipcodes})

@app.route('/download_csv', methods=['GET'])
def download_data():
    if not redis.exists('selected_dataset'):
        return "No table has been selected. Please select a table before trying to download data."
    dataset_name = redis.get('selected_dataset').decode()

    dataset_download = Read_Data(g.db)
    dataset_download.select_table(dataset_name)
    
    if redis.exists('selected_years'):
        years = json.loads(redis.get('selected_years').decode())
        if years:
            if len(years) == 2:
                dataset_download.filter_by_year(year1 = years[0], year2 = years[1])
            elif len(years) == 1:
                dataset_download.filter_by_year(year1 = years[0], year2 = None)

    if redis.exists('selected_zipcodes'):
        zipcodes = json.loads(redis.get('selected_zipcodes').decode())
        if zipcodes:
            dataset_download.filter_by_zipcode(zipcodes)
    dataset_download.build_query()
    filename = dataset_name + ".csv"
    filtered_data = dataset_download.run_query()
    # print(filtered_data)
    # print(type(filtered_data))
    file_dir_path = '/home/ra-terminal/Desktop/work/nycdohmh/projects/dataset_repo_api/data_db/data_files/'
    if filtered_data is not None:
        filtered_data.to_csv(f"{file_dir_path}/{filename}", index=False)
    else:
        print("Filtered data is None. No CSV file was created.")
    return send_from_directory(file_dir_path, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
    pass