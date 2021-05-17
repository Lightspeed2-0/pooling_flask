import math
import pgeocode
import requests
import json


def cordinatesDistance(lat1, lon1, lat2, lon2) :
    R = 6373.0
    
    lat1 = math.radians(52.2296756)
    lon1 = math.radians(21.0122287)
    lat2 = math.radians(52.406374)
    lon2 = math.radians(16.9251681)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return round(distance) 


def getCordinates(srcPincode,desPincode) :
    latitudearr = []
    longitudearr = []
    nomi = pgeocode.Nominatim('in')
    res = nomi.query_postal_code([srcPincode,desPincode])
    latitudearr = res.loc[:,"latitude"]
    longitudearr = res.loc[:,"longitude"]
    return { 'src' : [latitudearr[0],longitudearr[0]],'des' : [latitudearr[1],longitudearr[1]]}


def getPaths(srcPincode,desPincode) :
    path = []
    coordinatesGot = getCordinates(srcPincode,desPincode)
    # print(coordinatesGot)
    url = "https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf624841b747b534394a73b8283ad3de48ff61&start="+str(coordinatesGot['src'][1])+","+str(coordinatesGot['src'][0])+"&"+"end="+str(coordinatesGot['des'][1])+","+str(coordinatesGot['des'][0])
    print(url)
    req = requests.get(url)
    res = json.loads(req.text)
    geometry = res['features'][0]['geometry']
    path = geometry['coordinates']
    return path


# print(getPaths("606601","600044"))
# coord = getCordinates("605602","600063")

# print(cordinatesDistance(coord['src'][0],coord['src'][1],coord['des'][0],coord['des'][1]))
