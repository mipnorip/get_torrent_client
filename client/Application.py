import os
import configparser

import requests

class Application:
    def __init__(self) -> None: 
        config = configparser.ConfigParser()
        config.read('../config.ini')
        self.config = config['AUTHENTICATION']
        
        self.session = requests.Session()

    def get_list(self, name) -> dict:
        result = {}
        return result


    def get_items(self, path) -> None:
        pass
