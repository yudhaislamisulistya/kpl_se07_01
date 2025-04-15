# from config_env import get_base_url
from config_json import get_base_url

import requests

def main():
    base_url = get_base_url()
    try:
        response = requests.get(f"{base_url}/data")
        if response.status_code == 200:
            print("Data fetched successfully:", response.json())
        else:
            print("Failed to fetch data:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)
        
if __name__ == "__main__":
    main()