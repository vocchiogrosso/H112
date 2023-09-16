from algo.classes.TruckClass import Truck

# Create a truck
truck = Truck(1, "Delivery Truck", 1000)

# Start a delivery
truck.start_working("Delivery to Client A")

# Simulate some time passing (e.g., 2 hours)
# In a real application, you'd update the occupied_percentage based on actual working time
# Here, we're just simulating the passage of time.
import time
time.sleep(2 * 3600)  # Sleep for 2 hours

# Complete the delivery
truck.complete_delivery()

# Check the truck's attributes
print(f"Truck ID: {truck.truck_id}")
print(f"Truck Type: {truck.truck_type}")
print(f"Capacity: {truck.capacity} kg")
print(f"Occupied Percentage: {truck.occupied_percentage}%")
print(f"Current Delivery: {truck.current_delivery}")
