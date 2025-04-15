import json

ip = "192.168.1.1"

with open('config.json', 'r') as f:
    config = json.load(f)
    ip = config['serverIP']
    
print(f"Server IP: {ip}")