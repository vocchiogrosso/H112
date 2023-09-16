from classes.RouteClass import InboundRoute, OutboundRoute
from classes.TruckClass import Truck
from classes.LocationClass import Location, PlantLoc, ProviderLoc, ClientLoc

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