
# AI Pipeline Manager

AI Pipeline Manager is a Python library for creating and managing pipelines between various generative AI tools. It provides a flexible and extensible framework for chaining multiple AI tools together to create complex workflows.

## Installation

```bash
pip install ai-pipeline-manager
```

## Usage

```python
from ai_pipeline_manager import Pipeline, GroqTool, StableDiffusionTool

# Create a pipeline with Groq and Stable Diffusion tools
pipeline = Pipeline([GroqTool(), StableDiffusionTool()])

# Run the pipeline
input_text = "Generate a detailed description of a futuristic city, then create an image based on that description."
result = pipeline.run(input_text)

print("Pipeline result:", result)
```

## Adding New Tools

To add a new tool, create a new directory under `ai_pipeline_manager/tools/` and implement the `ToolInterface`. Then, update the `__init__.py` files and add any necessary configurations.

## Configuration

Create a `config.yaml` file in the root directory with the following structure:

```yaml
groq:
  api_key: your_groq_api_key

stable_diffusion:
  api_url: https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image
  api_key: your_stable_diffusion_api_key
```

## License

This project is licensed under the MIT License.
