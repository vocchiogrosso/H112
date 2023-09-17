import json

class MaterialManager:
    def __init__(self, materials=None, material_suppliers=None, seasonal_multipliers=None, material_multipliers=None, demand_thresholds=None, demand_multipliers=None):
        self.materials = materials if materials else {}
        self.material_suppliers = material_suppliers if material_suppliers else {}
        self.seasonal_multipliers = seasonal_multipliers if seasonal_multipliers else {}
        self.material_multipliers = material_multipliers if material_multipliers else {}
        self.demand_thresholds = demand_thresholds if demand_thresholds else []
        self.demand_multipliers = demand_multipliers if demand_multipliers else []

    @classmethod
    def from_json_file(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        
        flattened_data = {}
        material_suppliers = {}
        for category, materials in data.items():
            for material_id, info in materials.items():
                flattened_data[material_id] = 0  # Default demand
                material_suppliers[material_id] = info['Material']  # Supplier
        
        return cls(materials=flattened_data, material_suppliers=material_suppliers)

    def add_materials(self, materials_dict):
        for material_id, (supplier, demand) in materials_dict.items():
            if material_id in self.materials:
                print(f"Material '{material_id}' already exists. Updating its demand.")
                self.materials[material_id] += demand
                self.material_suppliers[material_id] = supplier  # Update supplier as well
            else:
                self.materials[material_id] = demand
                self.material_suppliers[material_id] = supplier
        print(f"Materials added/updated: {materials_dict}")

    def query(self, m, season="summer"):
        # Check if m is a supplier name
        if m not in self.materials:
            matching_ids = [id for id, supplier in self.material_suppliers.items() if supplier == m]
            if not matching_ids:
                raise ValueError(f"No materials found for supplier '{m}' or ID '{m}'.")
            if len(matching_ids) > 1:
                print(f"Multiple IDs found for supplier '{m}': {', '.join(matching_ids)}")
                m = input("Please choose one ID: ")
            else:
                m = matching_ids[0]

        demand = self.materials.get(m, 0)
        
        if not self.demand_multipliers:
            raise ValueError("Demand multipliers list is empty. Please initialize it with some values.")
        
        demand_multiplier = self.demand_multipliers[-1]  # default to the highest multiplier
        for i, threshold in enumerate(self.demand_thresholds):
            if demand <= threshold:
                demand_multiplier = self.demand_multipliers[i]
                break
                
        weight = demand * demand_multiplier * self.get_seasonal_multiplier(season) * self.get_material_multiplier(m)
        return weight

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

if __name__ == "__main__":

    manager = MaterialManager.from_json_file('infoMaterials.json')

    # 1. Adding new materials
    print("\n1. Adding new materials:")
    manager.add_materials({"10000071": ("CENIZA VOLANTE", 50), "10000088": ("ESCORIA", 30)})

    # 2. Setting demands for materials
    print("\n2. Setting demands:")
    manager.set_demands({"10000071": 70, "10000088": 35})

    # 3. Updating materials
    print("\n3. Updating materials:")
    manager.update_materials([("10000071", 10), ("10000088", -5)])

    # 4. Setting multipliers
    print("\n4. Setting multipliers:")
    manager.set_multiplier("seasonal", "winter", 0.9)
    manager.set_multiplier("material", "10000071", 1.2)

    # 5. Setting thresholds and multipliers
    print("\n5. Setting thresholds and multipliers:")
    manager.set_thresholds([10, 50, 100], [1.1, 1.3, 1.5, 1.7])

    # 6. Querying weights across different seasons
    print("\n6. Querying weights across different seasons:")
    seasons = ["summer", "winter", "monsoon"]
    for season in seasons:
        print(f"\nFor {season.capitalize()}:")
        for material in ["10000071", "10000088"]:
            print(f"Weight for {material}: {manager.query(material, season)}")

    # 7. Deleting materials
    print("\n7. Deleting materials:")
    manager.delete_materials(["10000071"])

    # 8. Querying after deletion
    print("\n8. Querying after deletion:")
    for season in seasons:
        print(f"\nFor {season.capitalize()}:")
        for material in ["10000088"]:
            print(f"Weight for {material}: {manager.query(material, season)}")

    # 9. Adding back materials and querying
    print("\n9. Adding back materials and querying:")
    manager.add_materials({"10000071": ("CENIZA VOLANTE", 55)})
    for season in seasons:
        print(f"\nFor {season.capitalize()}:")
        for material in ["10000071", "10000088"]:
            print(f"Weight for {material}: {manager.query(material, season)}")

    # 10. Edge case: Querying a material not in the list
    print("\n10. Edge case: Querying a material not in the list:")
    try:
        print(f"Weight for 99999999 in summer: {manager.query('99999999', 'summer')}")
    except ValueError as e:
        print(e)
