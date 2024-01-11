import base64
import io
import time
from diffusers import DiffusionPipeline



class ModelHandler:

    def __init__(self, hf_model_id) -> None:
        self.hf_model_id = hf_model_id

    def save_model_locally(self, local_path):
        """
        Loads the model from huggingfaces and saves it locally
         Args:
        - local_path (str): The local directory path where the model will be saved.
        """
        pipeline = DiffusionPipeline.from_pretrained(self.hf_model_id)
        pipeline.save_pretrained(local_path)
        self.local_path = local_path

    def test_local_model(self,prompt : str) -> str:
        """
        Test the locally saved DiffusionPipeline model by generating an image based on the provided prompt.

        Args:
        - prompt (str): The text prompt used to generate the image.

        Returns:
        - str: Base64 encoded representation of the generated image.
        """
        loaded_pipeline = DiffusionPipeline.from_pretrained(self.local_path)
        result = loaded_pipeline(prompt).images[0]
        image_bytes = io.BytesIO()
        result.save(image_bytes, format='PNG') 
        image_bytes = image_bytes.getvalue()
        base64_encoded = base64.b64encode(image_bytes).decode('utf-8')
        return base64_encoded



if __name__ == "__main__":
    mh = ModelHandler("nota-ai/bk-sdm-tiny-2m")
    mh.save_model_locally("test_model")
    prompt = "An astronaut riding a horse on the moon"
    mh.test_local_model(prompt)