from datetime import datetime
from RouteClass import Route, InboundRoute, OutboundRoute

class Truck:
    def __init__(self, truck_id, truck_type, capacity):
        self.truck_id = truck_id
        self.truck_type = truck_type
        self.capacity = capacity
        self.occupied = 0  # Initially, the truck is empty / kg
        self.worked = None  # Initially, the truck has not worked / hours
        self.current_delivery = {}  # What material the truck is currently delivering

    def new_working(self, current_delivery, weight, route):
        if self.worked is None:
            self.worked = route.distance / 50
        else:
            if self.worked + route.distance / 50 > 10:
                raise ValueError("Truck cannot work more than 10 hours per day.")

        if self.capacity < weight + self.occupied:
            raise ValueError("Truck is over capacity.")

        if self.current_delivery.get(current_delivery) is None:
            self.current_delivery.update({current_delivery: weight})
        else:
            self.current_delivery[current_delivery] += weight

        self.occupied = weight
    
    def complete_delivery(self):
        if self.worked is None:
            raise ValueError("Truck is not in use.")

        # Calculate the time the truck was in use
        end_time = datetime.now()
        working_time = end_time - self.worked

        # Reset the worked time and current delivery
        self.worked = None
        self.current_delivery = {}
        self.occupied = 0

def lambda_handler(event, context):
    # Here you can write code to handle the lambda event
    # For example, you can create a Truck object and call its methods
    # based on the data in the event parameter.
    pass