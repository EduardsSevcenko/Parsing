import requests
import json
import pandas as pd

user='eduardssevcenko'
API_TOKEN='ATOKEN'
url='https://api.github.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

url = 'https://api.github.com/'
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json())

pd.DataFrame(response).to_json('response.json')