import base64
import io
import logging
import sys
import threading
from flask import Flask, jsonify, request
from diffusers import DiffusionPipeline
import time
import os
import psutil


pid = os.getpid()

app = Flask(__name__)
job_pipeline = {

}
logging.basicConfig(level=logging.DEBUG)


def get_available_memory():
    memory_info = psutil.virtual_memory()
    return memory_info.available / (1024 ** 2)


def update_pipeline():

    waiting_jobs = [job for job_id, job in job_pipeline.items()
                    if job_pipeline[job_id]["status"] == "queued"]
    print(waiting_jobs)
    min_job = min(waiting_jobs, key=lambda job: int(job["job_id"]))
    min_job["status"] = "processing"
    run_job(min_job["job_id"], min_job["prompt"])


class ModelHandler:
    def __init__(self, handler_id: str, pipe: DiffusionPipeline):
        self.handler_id: str = handler_id
        self.pipeline = pipe

    def custom_callback(self, pipe, step_index, timestamp, callback_kwargs):
        # Total Inference steps = pipe.scheduler.num_inference_stesps , aktueller step = step_index
        job_pipeline[self.handler_id]["total_steps"] = pipe.scheduler.num_inference_steps
        job_pipeline[self.handler_id]["current_step"] = step_index
        app.logger.info(
            f"Call ID: {self.handler_id}, step_index : {step_index} timestamp {timestamp}")
        app.logger.info(job_pipeline)
        app.logger.debug(
            f"Memory free after step: {step_index} of call {self.handler_id}: {get_available_memory()}")
        return callback_kwargs

    def predict_on_model(self, prompt):
        app.logger.info(
            f"Predicting on {self.handler_id} with prompt :{prompt}")
        return self.pipeline(prompt, callback_on_step_end=self.custom_callback).images[0]

    def predict_async(self, prompt):
        app.logger.info(
            f"Predicting on {self.handler_id} with prompt :{prompt}")
        try:
            result = self.predict_on_model(prompt)
            image_bytes = io.BytesIO()
            result.save(image_bytes, format='PNG')
            image_bytes = image_bytes.getvalue()
            base64_encoded = base64.b64encode(image_bytes).decode('utf-8')
            job_pipeline[self.handler_id] = {"job_id": self.handler_id,
                                             "status": "completed", "result": base64_encoded, "prompt": prompt}
            update_pipeline()
        except ValueError as ve:
            job_pipeline[self.handler_id] = {"job_id": self.handler_id,
                                             "status": "failed", "error": str(ve), "prompt": prompt}


@app.route("/status/<job_id>", methods=["GET"])
def get_status(job_id):
    app.logger.info(job_pipeline)
    if job_id in job_pipeline:
        res = job_pipeline[job_id]
        if job_pipeline[job_id]["result"] is not None:
            res = job_pipeline.pop(job_id)
        return jsonify(res)
    else:
        return jsonify({"error": f"Job with ID {job_id} not found"}), 404


@app.route("/status", methods=["GET"])
def get_all_status():
    return job_pipeline


def run_job(request_id, prompt):
    pipe = DiffusionPipeline.from_pretrained("test_model")
    app.logger.info(f"request_id {request_id}")
    model_handler = ModelHandler(request_id, pipe)
    job_pipeline[request_id] = {"job_id": request_id,
                                "status": "processing", "result": None, "prompt": prompt}
    threading.Thread(
        target=model_handler.predict_async, args=(prompt,)).start()


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        data = request.get_json()
        app.logger.info(data)
        if "prompt" in data:
            prompt = data["prompt"]
            request_id = str(hash(time.time_ns()))
            if get_available_memory() > 7000:  # or Just get_nr of running jobs <= 3
                pipe = DiffusionPipeline.from_pretrained("test_model")
                app.logger.info(f"request_id {request_id}")
                model_handler = ModelHandler(request_id, pipe)
                job_pipeline[request_id] = {"job_id": request_id,
                                            "status": "processing", "result": None, "prompt": prompt}
                threading.Thread(
                    target=model_handler.predict_async, args=(prompt,)).start()
            else:
                job_pipeline[request_id] = {"job_id": request_id,
                                            "status": "queued", "result": None, "prompt": prompt}
                return jsonify({"job_id": request_id, "status": "queued", "prompt": prompt})
            return jsonify({"job_id": request_id, "status": "processing", "prompt": prompt})
        return jsonify({"error": "Missing 'prompt' in the request"}), 400


if __name__ == "__main__":
    app.run(debug=True)
