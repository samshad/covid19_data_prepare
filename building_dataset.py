import pandas as pd

df = pd.read_csv('Data/dataset_v5.0.csv')

cities = list(set(df['province/state']))
arr = []

for city in cities:
    tf = df[df['province/state'] == city]
    trr = []
    for index, row in tf.iterrows():
        trr.append([row['reporting date'], row['province/state'], row['country/region'],
                    row['latitude'], row['longitude'], row['confirmed'], row['deaths'], row['recovered']])

    sz = len(trr)
    trr.reverse()
    for i in range(sz-1):
        trr[i][5] -= trr[i+1][5]
        trr[i][6] -= trr[i+1][6]
        trr[i][7] -= trr[i+1][7]
    trr.reverse()
    for t in trr:
        arr.append(t)

fdf = pd.DataFrame(arr, columns=['reporting date', 'province/state', 'country/region', 'latitude',
                                 'longitude', 'confirmed', 'deaths', 'recovered'])
fdf.to_csv('Data/dataset_v6.0.csv', index=False)


