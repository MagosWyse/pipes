
from abc import ABC, abstractmethod

class ToolInterface(ABC):
    @abstractmethod
    def process(self, input_data):
        pass

    @abstractmethod
    def get_output_type(self):
        pass
