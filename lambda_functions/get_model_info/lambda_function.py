import json
import requests
from bs4 import BeautifulSoup


huggingface_base_url = "https://huggingface.co/api/models/"
bearer_token = "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"
arxiv_url = "https://arxiv.org/abs/"


def lambda_handler(event, context):
    model_id = event["model_id"]

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {bearer_token}'
    }

    api_url = huggingface_base_url + model_id
    response_data = {}

    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code // 100 == 2:
            api_response = response.json()
            response_data["HuggingFace_Info"] = get_hugging_face_info(
                api_response)
        else:
            print(
                f"API Call failed with status code: {response.status_code} and error {response.json()['error']}")
            return {
                "status_code": response.status_code,
                "body": {
                    "data": response.json()["error"]
                }}

        arxiv_id = get_archive_id(response.json())
        response_data["Arxiv_info"] = None
        if arxiv_id is not None:
            arxiv_call = requests.get(f"{arxiv_url}{arxiv_id}", headers={
                                      "Accept": "application/json"})
            arxiv_info = None
            if arxiv_call.status_code // 100 == 2:
                arxiv_text = arxiv_call.text
                arxiv_info = filter_paper_info(arxiv_text)
                response_data["Arxiv_info"] = arxiv_info

    except Exception as e:
        print(f"Error making API call: {e}")
        return {
            "status_code": 500,
            "body": {
                "data": e
            }}
    return {
        'statusCode': 200,
        'body': json.dumps({
            "data": response_data}
        )
    }


def get_archive_id(api_response: dict):
    tags = api_response.get("tags", [])
    if len(tags) > 0:
        arxiv_element = next(x for x in tags if x.startswith('arxiv'))
        return arxiv_element.split(":")[1]
    else:
        return None


def get_hugging_face_info(api_response: dict):
    return {
        "Task": api_response["pipeline_tag"],
        "Downloads": api_response["downloads"],
        "Likes": api_response["likes"],
        "Library Name": api_response["library_name"]
    }


def filter_paper_info(arxiv_text: str) -> dict:
    soup = BeautifulSoup(arxiv_text, features="html.parser")
    author_tag = soup.find(class_="authors")
    authors = author_tag.text.strip().removeprefix("Authors:")
    title_tag = soup.find(class_="title mathjax")
    title = title_tag.text.strip().removeprefix("Title:")
    abstract_tag = soup.find(class_="abstract mathjax")
    abstract = abstract_tag.text.strip().removeprefix("Abstract:")
    return {"Authors": authors, "Title": title, "Abstract": abstract}


def invoke_function():
    event = {
        "model_id": "latent-consistency/lcm-lora-sdxl"
    }
    resp = lambda_handler(event, None)
    print(resp)


invoke_function()
