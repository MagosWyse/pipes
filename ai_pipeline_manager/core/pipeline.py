
from typing import List
from .tool_interface import ToolInterface

class Pipeline:
    def __init__(self, tools: List[ToolInterface]):
        self.tools = tools

    def run(self, input_data):
        result = input_data
        for tool in self.tools:
            result = tool.process(result)
            print(result)
        return result

    def add_tool(self, tool: ToolInterface):
        self.tools.append(tool)

    def remove_tool(self, tool: ToolInterface):
        self.tools.remove(tool)
