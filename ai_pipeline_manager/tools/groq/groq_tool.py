
import groq
from ...core.tool_interface import ToolInterface
from ...utils.config import load_config

class GroqTool(ToolInterface):
    def __init__(self):
        config = load_config()
        self.client = groq.Client(api_key=config['groq']['api_key'])

    def process(self, input_data):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": input_data,
                }
            ],
            model="mixtral-8x7b-32768",
        )
        return chat_completion.choices[0].message.content

    def get_output_type(self):
        return str
