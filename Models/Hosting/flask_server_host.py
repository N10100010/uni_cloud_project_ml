import base64
import io
import logging
from flask import Flask, jsonify, request
from diffusers import DiffusionPipeline
import time


app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


class ModelHandler:
    def __init__(self, handler_id: str, pipe: DiffusionPipeline):
        self.handler_id: str = handler_id
        self.pipeline = pipe.to("cuda")

    def predict_on_model(self, prompt):
        app.logger.info(
            f"Predicting on {self.handler_id} with prompt :{prompt}")
        result = self.pipeline(prompt).images[0]
        image_bytes = io.BytesIO()
        result.save(image_bytes, format='PNG')
        image_bytes = image_bytes.getvalue()
        base64_encoded = base64.b64encode(image_bytes).decode('utf-8')
        return base64_encoded


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        data = request.get_json()
        app.logger.info(data)
        if "prompt" in data:
            prompt = data["prompt"]
            request_id = str(hash(time.time_ns()))
            pipe = DiffusionPipeline.from_pretrained("test_model")
            app.logger.info(f"request_id {request_id}")
            model_handler = ModelHandler(request_id, pipe)
            image_base64 = model_handler.predict_on_model(prompt)
            return jsonify({"job_id": request_id, "status": "finished", "prompt": prompt, "image": image_base64})
        return jsonify({"error": "Missing 'prompt' in the request"}), 400


@app.route("/test")
def test():
    return "test"


if __name__ == "__main__":
    app.run()
