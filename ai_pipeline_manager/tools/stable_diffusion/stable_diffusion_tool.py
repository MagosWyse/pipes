import requests
import io
from PIL import Image
from ...core.tool_interface import ToolInterface
from ...utils.config import load_config

class StableDiffusionTool(ToolInterface):
    def __init__(self):
        config = load_config()
        self.api_url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
        self.api_key = config['stable_diffusion']['api_key']

    def process(self, input_data):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "image/*"
        }
        
        data = {
            "prompt": input_data,
            "output_format": "png",  # You can change this to "jpeg" if preferred
        }
        
        files = {"none": ''}  # This empty file is required by the API
        
        response = requests.post(self.api_url, headers=headers, data=data, files=files)
        
        if response.status_code == 200:
            # The response content is the image data
            image = Image.open(io.BytesIO(response.content))
            
            # Save the image to a file
            output_path = "C:/Users/MONSTER/Pictures/pipes_images/generated_image.png"  # or .jpg if you chose jpeg format
            image.save(output_path)
            
            return f"Image generated and saved as {output_path}"
        else:
            raise Exception(f"Error from Stable Diffusion API: {response.text}")

    def get_output_type(self):
        return str  # Returns a string with the path to the saved image