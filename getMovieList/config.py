import json
import os

class Config:
    def __init__(self, configfile="config.json"):
        config_path = os.path.join(os.path.dirname(__file__), configfile)

        config = json.load(open(config_path, "r"))
        self.api_key = config["api_key"]
