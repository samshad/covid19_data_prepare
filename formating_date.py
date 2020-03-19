import pandas as pd


def get_string(s):
    ret = s.split('/')
    for _ in range(len(ret)):
        ret[_] = ret[_].strip()
    return ret


df = pd.read_csv('New folder/covid_19_data.csv')
arr = []

for index, row in df.iterrows():
    s = get_string(row['ObservationDate'])
    new_date = s[1] + '-' + s[0] + '-' + '2020'

    arr.append([new_date, row['Province/State'], row['Country/Region'], row['Confirmed'], row['Deaths'], row['Recovered']])

fdf = pd.DataFrame(arr, columns=['reporting date', 'Province/State', 'Country/Region', 'Confirmed',
                                 'Deaths', 'Recovered'])
fdf.to_csv('Data/dataset_v3.0.csv', index=False)
