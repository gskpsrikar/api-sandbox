from flask import Flask, jsonify, request
from app_mock import mock_data


app = Flask(__name__)


@app.route('/mock_api/health_check', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})


@app.route('/mock_api/get_schema', methods=['GET'])
def get_mock_data_schema():
    path = request.json.get('path')
    with app.app_context():
        data = mock_data.get_schema(path=path)
        return jsonify(data)


@app.route('/mock_api/get_sample', methods=['GET'])
def get_mock_data_sample():
    path = request.json.get('path')
    with app.app_context():
        data = mock_data.get_sample_mock_data_record(path=path)
        return jsonify(data)


@app.route('/mock_api/send_mock_data', methods=['POST'])
def post_mock_data():
    data = {
        "path": request.json.get('path'),
        "wait_time": int(request.json.get('wait_time')),
        "number_of_records": int(request.json.get('number_of_records'))
    }
    try:
        data['target'] = request.json.get('target')
    except:
        data['target'] = None

    with app.app_context():
        mock_data.send_mock_data(**data)
        return jsonify({"status": 'ok'})


if __name__ == "__main__":
    app.run(debug=True)
