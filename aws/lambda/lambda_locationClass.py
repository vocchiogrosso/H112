from math import radians, sin, cos, sqrt, atan2
import json

def locationClass(lat1, lon1, lat2, lon2, units="miles"):
    if units == "km":
        R = 6371.0  # Earth radius in kilometers
    else:
        R = 3958.8  # Earth radius in miles

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

def lambda_handler(event, context):
    lat1 = float(event['lat1'])
    lon1 = float(event['lon1'])
    lat2 = float(event['lat2'])
    lon2 = float(event['lon2'])
    units = event.get('units', 'miles')
    
    distance = locationClass(lat1, lon1, lat2, lon2, units)
    
    return {
        'statusCode': 200,
        'body': json.dumps('The distance between the two points is ' + str(distance) + ' ' + units + '.')
    }
