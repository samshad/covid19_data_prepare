import requests
import json

with open('Data/Weather Data/997.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

if 'code' in data:
    print('paisi...')
