class MaterialManager:
    def __init__(self, materials=None, seasonal_multipliers=None, material_multipliers=None, demand_thresholds=None, demand_multipliers=None):
        self.materials = materials if materials else {}
        self.seasonal_multipliers = seasonal_multipliers if seasonal_multipliers else {}
        self.material_multipliers = material_multipliers if material_multipliers else {}
        self.demand_thresholds = demand_thresholds if demand_thresholds else []
        self.demand_multipliers = demand_multipliers if demand_multipliers else []
        
    def set_materials(self, materials_list):
        for material, demand in materials_list:
            self.materials[material] = demand
        print(f"Materials updated: {self.materials}")

    def update_materials(self, materials_list):
        for material, change_in_demand in materials_list:
            if material not in self.materials:
                raise ValueError(f"Material '{material}' not found in the list.")
            self.materials[material] += change_in_demand
        print(f"Materials updated: {self.materials}")

    def add_materials(self, materials_dict):
        for material, demand in materials_dict.items():
            if material in self.materials:
                print(f"Material '{material}' already exists. Updating its demand.")
                self.materials[material] += demand
            else:
                self.materials[material] = demand
        print(f"Materials added/updated: {materials_dict}")

    def delete_materials(self, materials_list):
        for material in materials_list:
            if material in self.materials:
                del self.materials[material]
                print(f"Material '{material}' deleted.")
            else:
                print(f"Material '{material}' not found.")
    def set_demands(self, demands_dict):
        for material, demand in demands_dict.items():
            self.materials[material] = demand
        print(f"Demands updated: {self.materials}")

    def set_thresholds(self, thresholds, multipliers):
        if len(thresholds) != len(multipliers) - 1:
            raise ValueError("The number of multipliers should be one more than the number of thresholds.")
        self.demand_thresholds = thresholds
        self.demand_multipliers = multipliers
        print(f"Thresholds set: {self.demand_thresholds}")
        print(f"Multipliers set: {self.demand_multipliers}")
        
    def set_multiplier(self, multiplier_type, name, value):
        if multiplier_type == "seasonal":
            self.seasonal_multipliers[name] = value
        elif multiplier_type == "material":
            self.material_multipliers[name] = value
        else:
            raise ValueError(f"Invalid multiplier type '{multiplier_type}'.")
        print(f"{multiplier_type.capitalize()} multipliers updated: {getattr(self, multiplier_type + '_multipliers')}")
        
    def get_seasonal_multiplier(self, season):
        return self.seasonal_multipliers.get(season, 1.0)

    def get_material_multiplier(self, material):
        return self.material_multipliers.get(material, 1.0)

    def get_relative_demand_multiplier(self, material):
        total_demand = sum(self.materials.values())
        if total_demand == 0:
            return 1.0
        relative_demand = self.materials.get(material, 0) / total_demand
        return 1 + relative_demand

    def query(self, m, season="summer"):
        demand = self.materials.get(m, 0)
        
        if not self.demand_multipliers:
            raise ValueError("Demand multipliers list is empty. Please initialize it with some values.")
        
        demand_multiplier = self.demand_multipliers[-1]  # default to the highest multiplier
        for i, threshold in enumerate(self.demand_thresholds):
            if demand <= threshold:
                demand_multiplier = self.demand_multipliers[i]
                break
        demand_multiplier = self.demand_multipliers[-1]
        for i, threshold in enumerate(self.demand_thresholds):
            if demand <= threshold:
                demand_multiplier = self.demand_multipliers[i]
                break
        weight = demand * demand_multiplier * self.get_seasonal_multiplier(season) * self.get_material_multiplier(m) * self.get_relative_demand_multiplier(m)
        return weight

manager = MaterialManager()

# 1. Adding new materials
print("\n1. Adding new materials:")
manager.add_materials({"iron": 60, "gold": 25, "silver": 40, "copper": 15})

# 2. Setting demands for materials
print("\n2. Setting demands:")
manager.set_demands({"iron": 70, "gold": 30, "silver": 45, "copper": 20})

# 3. Updating materials
print("\n3. Updating materials:")
manager.update_materials([("iron", 10), ("gold", -5), ("copper", 5)])

# 4. Setting multipliers
print("\n4. Setting multipliers:")
manager.set_multiplier("seasonal", "winter", 0.9)
manager.set_multiplier("material", "silver", 1.2)

# 5. Setting thresholds and multipliers
print("\n5. Setting thresholds and multipliers:")
manager.set_thresholds([10, 50, 100], [1.1, 1.3, 1.5, 1.7])

# 6. Querying weights across different seasons
print("\n6. Querying weights across different seasons:")
seasons = ["summer", "winter", "monsoon"]
for season in seasons:
    print(f"\nFor {season.capitalize()}:")
    for material in ["iron", "gold", "silver", "copper"]:
        print(f"Weight for {material}: {manager.query(material, season)}")

# 7. Deleting materials
print("\n7. Deleting materials:")
manager.delete_materials(["gold", "copper"])

# 8. Querying after deletion
print("\n8. Querying after deletion:")
for season in seasons:
    print(f"\nFor {season.capitalize()}:")
    for material in ["iron", "silver"]:
        print(f"Weight for {material}: {manager.query(material, season)}")

# 9. Adding back materials and querying
print("\n9. Adding back materials and querying:")
manager.add_materials({"gold": 28, "copper": 18})
for season in seasons:
    print(f"\nFor {season.capitalize()}:")
    for material in ["iron", "gold", "silver", "copper"]:
        print(f"Weight for {material}: {manager.query(material, season)}")

# 10. Edge case: Querying a material not in the list
print("\n10. Edge case: Querying a material not in the list:")
try:
    print(f"Weight for platinum in summer: {manager.query('platinum', 'summer')}")
except ValueError as e:
    print(e)
