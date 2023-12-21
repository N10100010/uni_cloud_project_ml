


if __name__ == '__main__':
    import json
    import requests

    response = requests.get(
        "https://bo7apkf9fg.execute-api.eu-central-1.amazonaws.com/TestStage?model_id=nota-ai/bk-sdm-tiny",
    )
    content = json.loads(response.content)

    print(content['body'])
