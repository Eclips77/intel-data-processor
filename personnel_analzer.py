def load_personnel_data():
    return [
    {"id": "P001", "name": "Smith", "rank": "Captain", "unit": "Alpha", "clearance": "Secret"},
    {"id": "P002", "name": "Johnson", "rank": "Lieutenant", "unit": "Bravo", "clearance": "TopSecret"},
    {"id": "P003", "name": "Williams", "rank": "Sergeant", "unit": "Alpha", "clearance":
    "Confidential"},
    {"id": "P004", "name": "Brown", "rank": "Major", "unit": "Charlie", "clearance": "Top Secret"}]

def filter_by_clearance(personnel ,clearance_level):
    return [p for p in personnel if p["clearance"] == clearance_level]

def group_by_unit(personnel):
    units = {}
    for person in personnel:
        unit= person["unit"]
        if unit not in units:
            units[unit] =[]
        units[unit].append(person["name"])
    return units
