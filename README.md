# uni_cloud_project_ml

## Definition of responses
```
# serialized
response_object: dict =  {
    status_code: int
    body: dict
}

--> body: dict = {
    data: typing.Union[list, list[dict], dict, dict[str, dict], ..., foobar.image, str, float, int],
    meta: dict?
}

--> data: dict = {
    # endpoint dependent

}


```



### run flask:

```
cd server
flask run --port=5001 --debug
```

### run vue:

```
cd client
npm run dev
```




# AWS Endpoints
- saveModelOutput
    - expects: byte-string representing an image // currently jpg
        - sample: json.dumps({"mime_type": "image/jpeg", "image": "/9j/4AAQSkZJRgABAQEAYABgAAD//gA7Q1JFQVRPUjog......."}})
    - returns: a timestamp of the BA-time, the image has been saved
        - sample: {
                    "data": "b'{"statusCode": 200, "body": "{"response": "1703254127702910397.jpg"}"}'",
                    "status": "success"
                  }
- generateModelOutput
    - expects: prompt string
        - sample: json.dumps({"data": "a cat and a dog"})
    - returns: byte-string representing an image // currently jpg
        - sample: {
                    "mime_type": "image/jpeg",
                    "image": "/9j/4AAQSkZJRgABAQEAYABgAAD//gA7Q1JFQVRPUjog......."
                  }

- getModelInfo
    - expects: an specific model ID
        - sample: (call to: ...) https://bo7apkf9fg.execute-api.eu-central-1.amazonaws.com/TestStage?model_id=nota-ai/bk-sdm-tiny-2m
    - returns: some dict
        - sample: {
                    "some relevant information": "text-to-image"
                  }
