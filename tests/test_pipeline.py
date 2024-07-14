
import unittest
import sys
import os

# Add the parent directory (PIPES) to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_pipeline_manager.core.pipeline import Pipeline
from ai_pipeline_manager.tools.groq.groq_tool import GroqTool
from ai_pipeline_manager.tools.stable_diffusion.stable_diffusion_tool import StableDiffusionTool

class TestPipeline(unittest.TestCase):
    def test_pipeline_creation(self):
        pipeline = Pipeline([GroqTool(), StableDiffusionTool()])
        self.assertEqual(len(pipeline.tools), 2)

    def test_pipeline_run(self):
        pipeline = Pipeline([GroqTool(), StableDiffusionTool()])
        result = pipeline.run("Generate an image of a cat")
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
