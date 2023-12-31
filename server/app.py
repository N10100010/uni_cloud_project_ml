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


# This is the creator we chose to support.
# With the set limitations for the free-trail from amazon, we cannot allow more than one model.
# We chose a model from this creator.
FIXED_CREATOR = "nota-ai"

# The token for HuggingFace
HF_BEARER_TOKEN = "Bearer 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"

def generate_response_object(status_code: int) -> dict:
    return {
        "status_code": status_code,
        "status_message": requests.status_codes._codes[status_code]
    }

@app.route('/')
def start():
    return """
        <!DOCTYPE html>
        <html lang="en">
        
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Your Web Page Title</title>
            <!-- Add any additional meta tags, link to stylesheets, or other head elements here -->
        </head>
        
        <body>
            <!-- Your page content goes here -->
            <h1> HI </h1>
        
            <script>
                // Your JavaScript code goes here
            </script>
        </body>
        
        </html>
    """


@app.route('/models_by_creator', methods=['GET', 'POST'])
def models_by_creator():
    """
    To simulate the actual use case, we limited the search to the creator 'nota-ai'.
    Other searches, resulting in text-to-image models may be implemented here.
    :return:
    """

    response = requests.get(
        "https://huggingface.co/api/models",
        params={"author": FIXED_CREATOR, "limit": 100, "full": "True", "config": "True"},
        headers={"Authorization": HF_BEARER_TOKEN}
    )
    response_object = generate_response_object(response.status_code)
    content = json.loads(response.content)

    response_object['data'] = content

    return jsonify(response_object)


@app.route('/model_by_id', methods=['PUT'])
def __model_by_id():
    """
    Supposed to give the detailed information of a model, based on the selected ID from the front-end.
    Here again, we must limit ourselves, due to the limitations opposed by the free-trial from Amazon.
    :param model_id: str - representing the ID of a model, prefixed by its creator.
        (nota-ai/specific-model-id)
    :return:
    """
    model_id = request.json.get('modelId')  # Assuming JSON data, adjust as needed

    response = requests.get(
        f"https://huggingface.co/api/models/{model_id}",
        params={},
        headers={"Authorization": HF_BEARER_TOKEN}
    )

    response_object = generate_response_object(response.status_code)
    content = json.loads(response.content)
    response_object['data'] = content
    return jsonify(response_object)


@app.route('/generate_image/<prompt>', methods=['PUT'])
def _generate_image(prompt):

    response = requests.put(  # make me a put
        url="https://openimagebucket.s3.eu-central-1.amazonaws.com/1703254127702910397.jpg",
        data={'text_prompt': prompt}

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



