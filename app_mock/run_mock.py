from flask import Flask, jsonify, request
import mock_data


app = Flask(__name__)


@app.route('/api/health_check', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})


@app.route('/api/mock_data/<int:count>', methods=['GET'])
def get_mock_data(count: int):
    with app.app_context():
        data = mock_data.generate_mock_data(count=count)
        return jsonify(data)


@app.route('/api/mock_data', methods=['POST'])
def post_mock_data():
    data = {
        "count": int(request.json.get('count')),
        "output_location": request.json.get('output_location')
    }
    print(data)

    with app.app_context():
        data = mock_data.generate_and_hit(**data)
        return jsonify(data)


if __name__ == "__main__":
    data = {
        "name": "name"
    }
    app.run(debug=True)
