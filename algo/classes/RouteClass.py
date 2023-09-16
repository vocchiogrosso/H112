class Route:
    def __init__(self, route_id, route_name, distance, freight_cost_per_ton):
        self.route_id = route_id
        self.route_name = route_name
        self.distance = distance
        self.freight_cost_per_ton = freight_cost_per_ton

class InboundRoute(Route):
    def __init__(self, route_id, route_name, supplier_code, plant_code, distance, freight_cost_per_ton):
        super().__init__(route_id, route_name, distance, freight_cost_per_ton)
        self.supplier_code = supplier_code
        self.plant_code = plant_code

class OutboundRoute(Route):
    def __init__(self, route_id, route_name, plant_code, client_code, distance, freight_cost_per_ton):
        super().__init__(route_id, route_name, distance, freight_cost_per_ton)
        self.plant_code = plant_code
        self.client_code = client_code
