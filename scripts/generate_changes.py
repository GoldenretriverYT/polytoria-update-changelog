import sys
from xml.etree import ElementTree as ET

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = {}
    for type_elem in root.findall('Type'):
        type_name = type_elem.get('Name')
        methods = {}
        properties = {}
        for method_elem in type_elem.findall('Method'):
            method_name = method_elem.get('Name')
            parameters = [(param.get('Name'), param.get('Type')) for param in method_elem.findall('Parameter')]
            methods[method_name] = parameters
        for property_elem in type_elem.findall('Property'):
            property_name = property_elem.get('Name')
            property_type = property_elem.get('Type')
            properties[property_name] = property_type
        data[type_name] = {'methods': methods, 'properties': properties}
    return data

def compare_versions(old_data, new_data):
    changes = []
    old_types = old_data.keys()
    new_types = new_data.keys()

    for type_name in new_types:
        if type_name not in old_data:
            changes.append(f'New type added: {type_name}')
            continue

        old_methods = old_data[type_name]['methods']
        new_methods = new_data[type_name]['methods']
        old_properties = old_data[type_name]['properties']
        new_properties = new_data[type_name]['properties']

        # Compare methods
        for method_name, parameters in new_methods.items():
            if method_name not in old_methods:
                changes.append(f'New method added in {type_name}: {method_name}')
            elif old_methods[method_name] != parameters:
                changes.append(f'Method {method_name} in {type_name} changed parameters')

        for method_name in old_methods:
            if method_name not in new_methods:
                changes.append(f'Method {method_name} removed from {type_name}')

        # Compare properties
        for property_name, property_type in new_properties.items():
            if property_name not in old_properties:
                changes.append(f'New property added in {type_name}: {property_name} of type {property_type}')
            elif old_properties[property_name] != property_type:
                changes.append(f'Property {property_name} in {type_name} changed type from {old_properties[property_name]} to {property_type}')

        for property_name in old_properties:
            if property_name not in new_properties:
                changes.append(f'Property {property_name} removed from {type_name}')

    for type_name in old_types:
        if type_name not in new_data:
            changes.append(f'Type removed: {type_name}')

    return changes

if __name__ == '__main__':
    old_file = sys.argv[1]
    new_file = sys.argv[2]
    changes_file = sys.argv[3]

    old_data = parse_xml(old_file)
    new_data = parse_xml(new_file)
    changes = compare_versions(old_data, new_data)

    with open(changes_file, 'w') as f:
        f.write('# Changes\n')
        for change in changes:
            f.write(f'- {change}\n')
