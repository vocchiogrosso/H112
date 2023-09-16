from math import radians, sin, cos, sqrt, atan2
class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def haversine(self, that, units="miles"):
        if units == "km":
            R = 6371.0  # Earth radius in kilometers
        else:
            R = 3958.8  # Earth radius in miles

        lat1 = self.latitude
        lon1 = self.longitude
        lat2 = that.latitude
        lon2 = that.longitude
        
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        return distance

class PlantLoc(Location):
    def __init__(self, plant_id, plant_name, latitude, longitude):
        super().__init__(latitude, longitude)
        self.plant_id = plant_id
        self.plant_name = plant_name
        self.location_type = "Plant"

class ClientLoc(Location):
    def __init__(self, client_id, latitude, longitude, city):
        super().__init__(latitude, longitude)
        self.client_id = client_id
        self.city = city
        self.location_type = "Client"

class ProviderLoc(Location):
    def __init__(self, provider_id, origin, latitude, longitude, material_code, material_name):
        super().__init__(latitude, longitude)
        self.provider_id = provider_id
        self.origin = origin
        self.material_code = material_code
        self.material_name = material_name
        self.location_type = "Provider"