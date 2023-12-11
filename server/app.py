import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

import logging
import json
import requests

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/models_by_creator', methods=['GET', 'POST'])
def models_by_creator():

    response_object = {'status': 'success'}

    response = requests.get(
        "https://huggingface.co/api/models",
        params={"search": "nota-ai", "limit": 10, "full": "True", "config": "True"},
        headers={"Authorization": "Bearer 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"}
    )
    content = json.loads(response.content)

    response_object['data'] = content

    return jsonify(response_object)


@app.route('/models_by_creator', methods=['GET', 'POST'])
def __models_by_creator():

    response_object = {'status': 'success'}

    response = requests.get(
        "https://huggingface.co/api/models/nota-ai/bk-sdm-tiny",
        params={},
        headers={"Authorization": "Bearer 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"}
    )
    content = json.loads(response.content)

    response_object['data'] = content

    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    return jsonify(response_object)


@app.route('/model_by_id', methods=['PUT'])
def model_by_id():
    response_object = {'status': 'success'}

    # Retrieve the modelId from the request body
    model_id = request.json.get('modelId')

    # Perform actions with the modelId as needed



    response_object['data'] = {'modelId': model_id}
    return jsonify(response_object)



@app.route('/model_by_id/<model_id>', methods=['PUT'])
def __model_by_id():

    if request.method == 'PUT':
        print()

    response_object = {'status': 'success'}

    response = requests.get(
        "https://huggingface.co/api/models/nota-ai/bk-sdm-tiny",
        params={},
        headers={"Authorization": "Bearer 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"}
    )
    content = json.loads(response.content)

    response_object['data'] = content

    return jsonify(response_object)


if __name__ == '__main__':
    app.run()



