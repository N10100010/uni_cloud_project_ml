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


def generate_response_object(status_code: int) -> dict:
    return {
        "status_code": status_code,
        "status_message": requests.status_codes._codes[status_code]
    }


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

    response = requests.get(
        "https://huggingface.co/api/models/nota-ai/bk-sdm-tiny",
        params={},
        headers={"Authorization": "Bearer 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"}
    )
    response_object = generate_response_object(response.status_code)

    content = json.loads(response.content)

    response_object['data'] = content

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
def _model_by_id():

    response = requests.get(
        "https://huggingface.co/api/models/nota-ai/bk-sdm-tiny",
        params={},
        headers={"Authorization": "Bearer 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"}
    )
    response_object = generate_response_object(response.status_code)
    content = json.loads(response.content)

    response_object['data'] = content

    return jsonify(response_object)


@app.route('/generate_image/<prompt>', methods=['PUT'])
def _generate_image(prompt):

    response = requests.get(  # make me a put
        url="https://openimagebucket.s3.eu-central-1.amazonaws.com/1703254127702910397.jpg"
        # , data={'text_prompt': prompt}

    )
    response_object = generate_response_object(response.status_code)

    response_object['prompt'] = prompt
    # response_object['data'] = {'base64String': str(response.content), 'mimeType': 'image/jpg'}
    response_object['data'] = {'url': 'https://openimagebucket.s3.eu-central-1.amazonaws.com/1703254127702910397.jpg'}
    return jsonify(response_object)


@app.route('/save_output/<image>', methods=['PUT'])
def save_model_output(image):
    response = requests.post(
        url="https://1l62es3fz3.execute-api.eu-central-1.amazonaws.com/test-stage/saveModelOutput"
        , data=json.dumps({"mime_type": "image/jpeg", "image": image})
    )
    response_object = generate_response_object(response.status_code)

    return response_object


@app.route('/test', methods=['GET'])
def __test():

    response = requests.get(
        url="https://openimagebucket.s3.eu-central-1.amazonaws.com/Baysion_Theorem.png"
    )

    #response = requests.put(
    #    #url="https://57lfpibw9j.execute-api.eu-central-1.amazonaws.com/test-stage/saveModelOutput"
    #      # url="https://1l62es3fz3.execute-api.eu-central-1.amazonaws.com/test-stage/saveModelOutput"
    #      url="https://1l62es3fz3.execute-api.eu-central-1.amazonaws.com/test-stage/generateModelOutput"
    #    , data={'text_prompt': 'test value'}
    #)

    response_object = generate_response_object(response.status_code)

    content = str(response.content)

    response_object['data'] = content

    return jsonify(response_object)


if __name__ == '__main__':
    app.run()



