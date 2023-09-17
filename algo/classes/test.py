import json

Route = lambda route_id, route_name, distance, freight_cost_per_ton: {'route_id': route_id, 'route_name': route_name, 'distance': distance, 'freight_cost_per_ton': freight_cost_per_ton}

InboundRoute = lambda route_id, route_name, supplier_code, plant_code, distance, freight_cost_per_ton: {**Route(route_id, route_name, distance, freight_cost_per_ton), 'supplier_code': supplier_code, 'plant_code': plant_code}

OutboundRoute = lambda route_id, route_name, plant_code, client_code, distance, freight_cost_per_ton: {**Route(route_id, route_name, distance, freight_cost_per_ton), 'plant_code': plant_code, 'client_code': client_code}

# Testing the lambda functions with some parameters
inbound_route = InboundRoute(1, "Route A", "SC123", "PC123", 100, 200)
outbound_route = OutboundRoute(2, "Route B", "PC123", "CC123", 150, 300)

# Serializing to JSON
print(json.dumps(inbound_route, indent=4))
# Output: JSON representation of the inbound route dictionary

print(json.dumps(outbound_route, indent=4))
# Output: JSON representation of the outbound route dictionary