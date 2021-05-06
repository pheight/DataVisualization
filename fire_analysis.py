import csv

from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high and low temperatures from this file.
    lats, lons, brights = [], [], []
    for row in reader:
        print(row)
        try:
            current_date = datetime.strptime(row[5], '%Y-%m-%d')
        except IndexError:
            print("No date provided")
        else:
            try:
                lat = float(row[0])
                long = float(row[1])
                bright = float(row[2])
                print(lat, long, bright)
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                lats.append(lat)
                lons.append(long)
                brights.append(bright)




'''
print(all_fire_data)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)
'''

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker': {
        'size': [bright/50 for bright in brights],
        'color': brights,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]
my_layout = Layout(title='Global Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')
