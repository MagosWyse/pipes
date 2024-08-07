import yaml
import os

def load_config():
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'config.yaml')
    with open(config_path, 'r') as config_file:
        return yaml.safe_load(config_file)
