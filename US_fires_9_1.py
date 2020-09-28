import json

bseptinfile = open('US_fires_9_1.json', 'r')
bseptoutfile = open('bsept_fire_data.json', 'w')
bseptdata = json.load(bseptinfile)
json.dump(bseptdata, bseptoutfile, indent = 4)

blons, blats, brightness = [], [], []

for x in bseptdata:
    lon = x['longitude']