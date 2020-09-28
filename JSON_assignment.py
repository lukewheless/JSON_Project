import json 

file_fires = open("c:Users/luke_wheless/Downloads/US_fires_9_14.json", "r")
fire = json.load(file_fires)
lats,lons,b = [],[],[]

for value in fire:
    lat = value["latitude"]
    lon = value['longitude']
    bright = value["brightness"]

    if bright == 450:
        b.append(bright)

    lats.append(lat)
    lons.append(lon)
    

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline 

data = [{

        "brightness": b, 
        "latitude": lats,
        'longitue': lons,
        "marker": {
            "size": [5*bright for bright in b],
        },
}]

my_layout = Layout(titles = "California Fires")

fig = {"data":data, "layout":my_layout}

offline.plot(fig, filename = "california_fires_html")

fig.show()