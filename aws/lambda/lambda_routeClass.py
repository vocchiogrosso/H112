import json

class Route:
    def __init__(self, event):
        self.route_id = event['route_id']
        self.route_name = event['route_name']
        self.distance = event['distance']
        self.freight_cost_per_ton = event['freight_cost_per_ton']

class InboundRoute(Route):
    def __init__(self, event):
        super().__init__(event)
        self.supplier_code = event['supplier_code']
        self.plant_code = event['plant_code']

class OutboundRoute(Route):
    def __init__(self, event):
        super().__init__(event)
        self.plant_code = event['plant_code']
        self.client_code = event['client_code']

def lambda_handler(event, context):
    inbound_route = InboundRoute(event).__dict__
    outbound_route = OutboundRoute(event).__dict__
    
    return {
        'statusCode': 200,
        'body': {
            'inbound_route': inbound_route,
            'outbound_route': outbound_route
        }
    }
