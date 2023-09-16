from LocationClass import PlantLoc, ClientLoc, ProviderLoc
from math import radians, sin, cos, sqrt, atan2

import json

plants = json.load(open("./data/infoPlants.json", "r"))
clients = json.load(open("./data/infoClients.json", "r"))
providers = json.load(open("./data/infoProviders.json", "r"))

c1 = clients["Outbound ARG"]
c1id = list(c1.keys())[0]
c1 = c1[list(c1.keys())[0]]
p1id = list(c1.keys())[0]
p1 = providers["Inbound ARG"]
p1 = p1[list(p1.keys())[0]]

print(c1)
print(p1)

import ipdb; ipdb.set_trace()
C1 = ClientLoc(c1id, c1["Latitude"], c1["Longitude"], c1["City"])
P1 = ProviderLoc(p1id, p1["Origin"], p1["Latitude"], p1["Longitude"], p1["Material Code"], p1["Material"])

print(C1.haversine(P1))
print(C1.client_id, C1.city)