from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route('/api/v1.0/test', methods=['GET'])
def testing():
    test = {
        "items": [
            { "id": 1, "name": "Apples",  "price": "$2" },
            { "id": 2, "name": "Peaches", "price": "$5" }
        ]
    }
    # test = 'This is the API response.'
    response = make_response(jsonify(test))

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    return response
