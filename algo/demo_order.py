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

def f(distance, material_weight, max_distance, order_weight, emission_rate, alpha=0.25, beta=0.35):

    normalized_distance = 1 - (distance / max_distance) if max_distance != 0 else 1
    normalized_weight = material_weight
    
    emissions = distance * material_weight * emission_rate
    max_emissions = max_distance * order_weight * emission_rate
    normalized_emissions = 1 - (emissions / max_emissions) if max_emissions != 0 else 1

    score = alpha * normalized_weight + (1 - alpha) * normalized_distance + beta * normalized_emissions
    return score

EMISSION_RATE = 0.123

def recommend_inbound(providers, materialMng, order):
    client = order.client
    dist = {}
    scores = {}
    for provider in providers:
        dist[provider] = client.haversine(provider)
    
    max_distance = max(dist.values())
    
    for provider in providers:
        scores[provider] = f(dist[provider], materialMng.query(provider.material_code), max_distance, order.weight, EMISSION_RATE)
    
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_scores[0][0]


materialMng = MaterialManager.from_json_file('infoMaterials.json')

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