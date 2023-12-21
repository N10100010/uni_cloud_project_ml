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