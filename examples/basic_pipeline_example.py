import sys
import os

# Add the parent directory (PIPES) to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_pipeline_manager.core.pipeline import Pipeline
from ai_pipeline_manager.tools.groq.groq_tool import GroqTool
from ai_pipeline_manager.tools.stable_diffusion.stable_diffusion_tool import StableDiffusionTool

def main():
    # Create a pipeline with Groq and Stable Diffusion tools
    pipeline = Pipeline([GroqTool(), StableDiffusionTool()])

    # Run the pipeline
    input_text = "Generate a detailed description of a futuristic city, then create an image based on that description."
    result = pipeline.run(input_text)

    print("Pipeline result:", result)

if __name__ == "__main__":
    main()