import json

bseptinfile = open('US_fires_9_1.json', 'r')
bseptoutfile = open('bsept_fire_data.json', 'w')
bseptdata = json.load(bseptinfile)
json.dump(bseptdata, bseptoutfile, indent = 4)

blons, blats, bbrightness = [], [], []

for x in bseptdata:
    lon = x['longitude']
    lat = x['latitude']
    bright = x['brightness']
    blons.append(lon)
    blats.append(lat)
    if bright > 450:
        bbrightness.append(bright)


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type' : 'scattergeo',
    'lon' : blons,
    'lat' : blats,
    'maker' : {
        'size' : [.05 * bright for bright in bbrightness],
        'color' : bbrightness,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Brightness'}
    },
}]

my_layout = Layout(title = 'Fires')

fig = {'data' : data, 'layout' : my_layout}

offline.plot(fig, filename = 'bed_sept_fires.html')