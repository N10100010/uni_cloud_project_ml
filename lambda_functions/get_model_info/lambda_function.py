import json
import requests
from bs4 import BeautifulSoup


huggingface_base_url = "https://huggingface.co/api/models/"
bearer_token = "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"
arxiv_url = "https://arxiv.org/abs/"


def lambda_handler(event, context):
    """
    MAIN
    """
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
            response_data["huggingface_info"] = get_hugging_face_info(
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
        response_data["arxiv_info"] = None
        if arxiv_id is not None:
            arxiv_call = requests.get(f"{arxiv_url}{arxiv_id}", headers={
                                      "Accept": "application/json"})
            arxiv_info = None
            if arxiv_call.status_code // 100 == 2:
                arxiv_text = arxiv_call.text
                arxiv_info = filter_paper_info(arxiv_text)
                arxiv_info["arxiv_id"] = arxiv_id
                response_data["arxiv_info"] = arxiv_info

    except Exception as e:
        print(f"Error making API call: {e}")
        return {
            "status_code": 500,
            "body": {
                "data": e
            }}
    return {
        'statusCode': 200,
        'body': {
            "data": response_data}
    }


def get_archive_id(api_response: dict):
    """
    EXTRACT THE ARXIV ID FROM THE HUGGING FACE RESPONSE.
    """
    tags = api_response.get("tags", [])
    if len(tags) > 0:
        arxiv_element = next(x for x in tags if x.startswith('arxiv'))
        return arxiv_element.split(":")[1]
    else:
        return None


def get_hugging_face_info(api_response: dict):
    """
    EXTRACT RELEVANT INFORMATION FROM THE API RESPONSE OF HUGGING FACE.
    """
    return {
        "task": api_response["pipeline_tag"],
        "downloads": api_response["downloads"],
        "likes": api_response["likes"],
        "library_name": api_response["library_name"]
    }


def filter_paper_info(arxiv_text: str) -> dict:
    """
    EXTRACT RELEVANT INFORMATION FROM THE RESPECTIVE PAPER PAGE FROM ARXIV.
    """
    soup = BeautifulSoup(arxiv_text, features="html.parser")
    author_tag = soup.find(class_="authors")
    authors = author_tag.text.strip().removeprefix("Authors:")
    title_tag = soup.find(class_="title mathjax")
    title = title_tag.text.strip().removeprefix("Title:")
    abstract_tag = soup.find(class_="abstract mathjax")
    abstract = abstract_tag.text.strip().removeprefix("Abstract:")
    return {"authors": authors, "title": title, "abstract": abstract}