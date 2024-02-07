from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from diffusers import DiffusionPipeline
import threading

app = Flask(__name__)
socketio = SocketIO(app)

class ModelHandler:
    def __init__(self, local_path):
        self.local_path = local_path
        self.pipeline : DiffusionPipeline = None

    def load_model(self):
        try:
            self.pipeline = DiffusionPipeline.from_pretrained(self.local_path)
            print(f"Num inference steps: {self.pipeline.num_inference_steps}")
        except Exception as e:
            raise ValueError(f"Error loading the model: {str(e)}")

    def predict_on_model(self, prompt):
        if self.pipeline is None:
            self.load_model()
        return self.pipeline(prompt).images[0]

model_handler = ModelHandler("test_model")  # Provide the actual local model path here

def predict_async(prompt, job_id):
    try:
        result = model_handler.predict_on_model(prompt)
        socketio.emit('prediction_result', {'job_id': job_id, 'status': 'completed', 'result': result.tolist()})
    except ValueError as ve:
        socketio.emit('prediction_result', {'job_id': job_id, 'status': 'failed', 'error': str(ve)})

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        data = request.get_json()

        if "prompt" in data:
            prompt = data["prompt"]

            # Generate a unique job ID
            job_id = hash(prompt)  # You may want to use a more robust method to generate unique IDs
            
            # Initialize job status
            socketio.emit('prediction_result', {'job_id': job_id, 'status': 'processing'})

            # Start a separate thread for prediction
            threading.Thread(target=predict_async, args=(prompt, job_id)).start()

            return jsonify({"job_id": job_id, "status": "processing"})

        return jsonify({"error": "Missing 'prompt' in the request"}), 400

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == "__main__":
    socketio.run(app, debug=True)