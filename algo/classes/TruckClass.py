from datetime import datetime
class Truck:
    def __init__(self, truck_id, truck_type, capacity):
        self.truck_id = truck_id
        self.truck_type = truck_type
        self.capacity = capacity
        self.occupied = 0  # Initially, the truck is empty / kg
        self.start_time = None  # The time the driver started working
        self.current_delivery = None  # What the truck is currently delivering

    def start_working(self, current_delivery):
        if self.start_time is not None:
            raise ValueError("Truck is already in use.")

        self.start_time = datetime.now()
        self.current_delivery = current_delivery

    def complete_delivery(self):
        if self.start_time is None:
            raise ValueError("Truck is not in use.")

        # Calculate the time the truck was in use
        end_time = datetime.now()
        working_time = end_time - self.start_time

        # Update the occupied percentage based on working time
        # (You may need to adjust this calculation based on your business logic)
        self.occupied_percentage += working_time.total_seconds() / 3600.0

        # Reset the start time and current delivery
        self.start_time = None
        self.current_delivery = None
        self.occupied_percentage = 0
