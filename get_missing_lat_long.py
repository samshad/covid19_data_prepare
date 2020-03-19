import pandas as pd
from geopy.geocoders import Nominatim
import math

geolocator = Nominatim()
df = pd.read_csv('Data/dataset_v3.0.csv')
arr = []

# location = geolocator.geocode('zabaikalsky')
# print(location.latitude, location.longitude)

location_dict = dict()

for index, row in df.iterrows():
    print('#######', row['Province/State'])
    if row['Province/State'] in location_dict:
        arr.append([row['reporting date'], row['Province/State'], row['Country/Region'],
                    location_dict[row['Province/State']][0], location_dict[row['Province/State']][1],
                    row['Confirmed'], row['Deaths'], row['Recovered']])
    else:
        location = geolocator.geocode(row['Province/State'], timeout=10)
        if location is not None:
            location_dict[row['Province/State']] = [location.latitude, location.longitude]
            arr.append([row['reporting date'], row['Province/State'], row['Country/Region'],
                        location.latitude, location.longitude, row['Confirmed'], row['Deaths'], row['Recovered']])
        else:
            arr.append([row['reporting date'], row['Province/State'], row['Country/Region'],
                        '', '', row['Confirmed'], row['Deaths'], row['Recovered']])

fdf = pd.DataFrame(arr, columns=['reporting date', 'Province/State', 'Country/Region', 'latitude',
                                 'longitude', 'Confirmed', 'Deaths', 'Recovered'])
fdf.to_csv('Data/dataset_v4.0.csv', index=False)
