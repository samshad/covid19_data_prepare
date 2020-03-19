import pandas as pd


def init():
    global no
    global arr
    no = 0
    arr = []


def formate_date(dt):
    ret = dt.split('-')
    return ret[0] + '-' + ret[1] + '-2020'


df = pd.read_csv('Data/final_dataset.csv')

no = 0
id = 1
cnt = 1

arr = []

for index, row in df.iterrows():
    arr.append([id, formate_date(row['reporting date']), row['province/state'], row['country/region'],
                row['latitude'], row['longitude'], row['confirmed'], row['deaths'], row['recovered']])
    id += 1
    no += 1
    if no > 800:
        fdf = pd.DataFrame(arr, columns=['id', 'reporting date', 'province/state', 'country/region', 'latitude',
                                         'longitude', 'confirmed', 'deaths', 'recovered'])
        fdf.to_csv('Data/Split Datas/dataset_' + str(cnt) + '.csv', index=False)
        init()
        cnt += 1

fdf = pd.DataFrame(arr, columns=['id', 'reporting date', 'province/state', 'country/region', 'latitude',
                                         'longitude', 'confirmed', 'deaths', 'recovered'])
fdf.to_csv('Data/Split Datas/dataset_' + str(cnt) + '.csv', index=False)
