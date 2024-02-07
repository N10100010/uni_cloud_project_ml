import requests
# cerebro: 141.62.74.5 (RTX2080Ti)
# hal9k: 141.62.74.4 (RTX2080Ti)
# jarvis: 141.62.74.1 (TITAN XP)
# tars: 141.62.74.14 (A6000) 5.7s

servers = {"cerebro": "141.62.74.5", "hal9k": "141.62.74.4",
           "jarvis": "141.62.74.1", "tars": "141.62.74.14"}


def call_model(data):
    for server_name, url in servers.items():
        try:
            response = requests.post(f"{url}/predict", data=data)
            response.raise_for_status()
            return response.body
        except requests.exceptions.RequestException as e:
            print(f"Request to {server_name} ({url}) failed: {e}")
    return None


def lambda_handler(event, context):

    prompt = event["prompt"]
    data = {"prompt": prompt}
    response = call_model(data)
    if response is None:
        return {
            "status_code": 500,
            "body": "Error: No Model Hosting server could be reached"
        }
    return {
        'status_code': 200,
        'body': response
    }
