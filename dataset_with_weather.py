import json
import pandas as pd

arr = []

for file in range(1, 6):
    print(file)
    df = pd.read_csv('Data/Split Datas/dataset_' + str(file) + '.csv')

    for index, r in df.iterrows():
        with open('Data/Weather Data/' + str(r['id']) + '.json', encoding='utf-8') as json_file:
            wdata = json.load(json_file)
        arr.append([r['reporting date'], r['province/state'], r['country/region'],
                    r['latitude'], r['longitude'], r['confirmed'], r['deaths'], r['recovered'],
                    wdata['daily']['data'][0]['temperatureMin'], wdata['daily']['data'][0]['temperatureMax'],
                    wdata['daily']['data'][0]['humidity'], wdata['daily']['data'][0]['windSpeed'],
                    wdata['daily']['data'][0]['cloudCover']])

fdf = pd.DataFrame(arr, columns=['reporting date', 'province/state', 'country/region', 'latitude',
                                 'longitude', 'confirmed', 'deaths', 'recovered', 'temperatureMin', 'temperatureMax',
                                 'humidity', 'windSpeed', 'cloudCover'])
fdf.to_csv('Data/dataset_weather.csv', index=False)
