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
    
    #... (all other methods here)
def lambda_handler(event, context):
    try:
        action = event['action']
        data = event.get('data', {})
        PATH = "../data/"
        manager = MaterialManager.from_json_file(PATH + 'infoMaterials.json')
        response = ''

        if action == 'add_materials':
            materials_dict = data.get('materials_dict', {})
            manager.add_materials(materials_dict)
            response = "Materials added/updated"

        elif action == 'set_demands':
            demands_dict = data.get('demands_dict', {})
            manager.set_demands(demands_dict)
            response = "Demands updated"

        elif action == 'update_materials':
            materials_list = data.get('materials_list', [])
            manager.update_materials(materials_list)
            response = "Materials updated"

        elif action == 'delete_materials':
            materials_list = data.get('materials_list', [])
            manager.delete_materials(materials_list)
            response = "Materials deleted"

        elif action == 'set_thresholds':
            thresholds = data.get('thresholds', [])
            multipliers = data.get('multipliers', [])
            manager.set_thresholds(thresholds, multipliers)
            response = "Thresholds and multipliers set"

        elif action == 'set_multiplier':
            multiplier_type = data.get('multiplier_type', '')
            name = data.get('name', '')
            value = data.get('value', 1.0)
            manager.set_multiplier(multiplier_type, name, value)
            response = "Multiplier set"

        elif action == 'query':
            material_id = data.get('material_id', '')
            season = data.get('season', 'summer')
            response = manager.query(material_id, season)

        else:
            raise ValueError(f"Invalid action: {action}")

        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }