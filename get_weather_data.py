import requests
import pandas as pd
import json


def get_data(dt, latitude, longitude, id):
    api = "8ae03ec85528d27e5a722550bb3bd4aa"
    url = "https://api.darksky.net/forecast/{}/{},{},{}?exclude=currently,hourly,flags"

    s = dt.split('-')
    dt = s[2] + '-' + s[1] + '-' + s[0]
    tm = str(dt) + 'T00:00:00Z'
    res = requests.get(url.format(api, latitude, longitude, tm)).json()

    if 'code' in res:
        return False
    else:
        with open('Data/Weather Data/' + str(id) + '.json', 'w') as json_file:
            json.dump(res, json_file, indent=4)
        return True


file_path = 'Data/Split Datas/dataset_5.csv'
df = pd.read_csv(file_path)

for index, r in df.iterrows():
    print(r['id'])
    #if int(r['id']) >= 2997:
    if not get_data(r['reporting date'], r['latitude'], r['longitude'], r['id']):
        print('gese', r['id'], '######')
        break

print('done...')
