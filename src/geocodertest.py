import geopy
from geopy.geocoders import Nominatim
import requests
import json

locator = Nominatim(user_agent='myGeocoder')
apartment = locator.geocode('Overgade, 5000 Odense, Odense C')
OB = locator.geocode('Odense, Roesskovsvej')

r = requests.get(f"http://router.project-osrm.org/route/v1/car/{apartment.longitude},{apartment.latitude};{OB.longitude},{OB.latitude}?overview=false")
routes = json.loads(r.content)
route_1 = routes.get("routes")[0]
print (route_1['distance'])
