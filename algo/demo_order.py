import sys
sys.path.append("algo/classes")
from RouteClass import InboundRoute, OutboundRoute
from TruckClass import Truck
from LocationClass import Location, PlantLoc, ProviderLoc, ClientLoc
from MaterialManagerClass import MaterialManager

import json

class Order:
    def __init__(self, material, weight, client, plant):
        self.material = material
        self.weight = weight
        self.client = client
        self.plant = plant

def recommend_inbound(providers, order):
    client = order.client
    dist = {}
    for provider in providers:
        # calculate the distance between the provider and the client
        dist[provider] = client.haversine(provider)
    
    # sort the distances
    # TODO: lambda can be replaced with a function
    dist = sorted(dist.items(), key=lambda x: x[1])
    
    # return the closest provider
    return dist[0][0]

PATH = "./data/"
tmp = json.load(open(PATH + "infoPlants.json", "r"))['Outbound ARG']
plants = []
for plant in tmp:
    print(plant)
    plants.append(PlantLoc(plant, tmp[plant]['Plant Name'], tmp[plant]['Latitude'], tmp[plant]['Longitude']))
print("")

tmp = json.load(open(PATH + "infoClients.json", "r"))['Outbound ARG']
clients = []
for client in tmp:
    print(client)
    clients.append(ClientLoc(client, tmp[client]['Latitude'], tmp[client]['Longitude'], tmp[client]['City']))
print("")

tmp = json.load(open(PATH + "infoProviders.json", "r"))['Inbound ARG']
providers = []
for provider in tmp:
    print(provider)
    providers.append(ProviderLoc(provider, tmp[provider]['Origin'], tmp[provider]['Latitude'], tmp[provider]['Longitude'], tmp[provider]['Material Code'], tmp[provider]['Material']))
print("")

v_order1 = Order("SLEEP, FOOD, AND CAT!!!", 10, clients[0], plants[0])    
rec = recommend_inbound(providers, v_order1)
print(rec.provider_id, rec.origin, rec.material_name, rec.material_code)
print("Plant: ", v_order1.plant.plant_id, v_order1.plant.plant_name, v_order1.plant.latitude, v_order1.plant.longitude)
print("Client: ", v_order1.client.client_id, v_order1.client.city, v_order1.client.latitude, v_order1.client.longitude)
print("Provider: ", rec.provider_id, rec.origin, rec.latitude, rec.longitude)
print(rec.haversine(v_order1.client))