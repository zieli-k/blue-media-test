import os
import datacollector


class Config:

    def __init__(self, env):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.json_path = os.path.join(ROOT_DIR, 'resources/config')
        self.env = env

    def get_config(self):
        return datacollector.get_json_data(self.json_path, self.env)

    def get_url(self):
        return self.get_config()['url']
