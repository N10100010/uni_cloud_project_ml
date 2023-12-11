


if __name__ == '__main__':
    import json
    import requests
    response_object = {'status': 'success'}

    response = requests.get(
        "https://huggingface.co/api/models",
        params={"search": "nota-ai", "limit": 10, "full": "True", "config": "True"},
        headers={"Authorization": "Bearer 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"}
    )
    content = json.loads(response.content)

    response_object['data'] = content

    print(response_object['data'] )
