import requests
import base64
import os

# Replace with your actual endpoint URL
url = "http://141.62.74.4:5000/predict"
data = {"prompt": "A dog jumping around in the snow in front of a beautiful mountain scenery in the background in a photorealistic style"}

# Send POST request
response = requests.post(url, json=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Decode the base64 image
    base64_image = response.json().get("image", "")
    if base64_image:
        # Save the image locally
        base64_image = base64_image.split(",")[1]
        image_data = base64.b64decode(base64_image)
        with open("output_image.png", "wb") as f:
            f.write(image_data)
        print("Image saved successfully as output_image.png")
    else:
        print("No image data in the response")
else:
    print(f"Error: {response.status_code} - {response.text}")
