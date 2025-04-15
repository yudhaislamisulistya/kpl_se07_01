import json

def get_base_url():
    with open('config.json', 'r') as file:
        config = json.load(file)
        return config['base_url']