import jason
from urllib.request import urlopen
html = urlopen("https://freegeoip.net/json/147.47.7.38")
deserialized = json.loads(html.read())
print({"ip":deserialized["ip"]})
print({"위도":deserialized["latitude"]})
print({"경도":deseriazed["longitude"]})
