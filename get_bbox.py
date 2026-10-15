import urllib.request
import json

url = "https://nominatim.openstreetmap.org/search?q=Garissa+County,Kenya&format=json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    response = urllib.request.urlopen(req)
    data = json.loads(response.read().decode())
    if data:
        bbox = data[0]['boundingbox']
        # bbox format from nominatim: [lat_min, lat_max, lon_min, lon_max]
        # we need [lon_min, lat_min, lon_max, lat_max]
        lat_min, lat_max, lon_min, lon_max = [float(x) for x in bbox]
        print(f"[{lon_min}, {lat_min}, {lon_max}, {lat_max}]")
    else:
        print("No results found.")
except Exception as e:
    print(f"Error: {e}")
