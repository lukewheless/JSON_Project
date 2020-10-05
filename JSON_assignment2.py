import json 

file_fires = open("US_fires_9_1.json", "r")
fire = json.load(file_fires)
lats,lons,b = [],[],[]

for value in fire:
    lat = value["latitude"]
    lon = value['longitude']
    bright = value["brightness"]

    if bright > 450:
        b.append(bright)
        lats.append(lat)
        lons.append(lon)

data = [{"type": "scattergeo",
        "lat": lats,
        'lon': lons,
        "marker": {
            "size": [0.03*bright for bright in b],
            "color": b,
            "colorscale": "Viridis",
            'reversescale': True,
            'colorbar':{"title":"brightness"}
        },
}]

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline 

my_layout = Layout(title="California Fires")

fig = {"data":data, "layout":my_layout}

offline.plot(fig, filename="california_fires.html")