import os

import datacollector


class Config:

    def __init__(self, name):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.json_path = os.path.join(ROOT_DIR, 'resources/test_data')
        self.name = name

    def get_config(self):
        return datacollector.get_json_data(self.json_path, self.name)
