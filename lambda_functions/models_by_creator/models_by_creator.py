import requests
import json

# This is the creator we chose to support.
# With the set limitations for the free-trail from amazon, we cannot allow more than one model.
# We chose a model from this creator.
FIXED_CREATOR = "nota-ai"
# The token for HuggingFace
HF_BEARER_TOKEN = "Bearer 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"


def lambda_handler(event, context):
    """
    MAIN
    """

    def generate_response_object(status_code: int) -> dict:
        return {
            "statusCode": status_code,
            "statusMessage": requests.status_codes._codes[status_code],
            "isBase64Encoded": False,
        }

    response = requests.get(
        "https://huggingface.co/api/models",
        params={"author": FIXED_CREATOR, "limit": 100, "full": "True", "config": "True"},
        headers={"Authorization": HF_BEARER_TOKEN}
    )
    response_object = generate_response_object(response.status_code)
    content = json.loads(response.content)

    response_object['body'] = content

    return str(json.dumps(response_object))
