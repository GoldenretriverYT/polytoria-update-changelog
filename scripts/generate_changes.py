import sys
from xml.etree import ElementTree as ET

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = {}
    base_types = {}
    for type_elem in root.findall('Type'):
        type_name = type_elem.get('Name')
        inherits_from = type_elem.get('InheritsFrom').split(".")[-1] if type_elem.get('InheritsFrom') else None
        
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
        
        type_data = {'methods': methods, 'properties': properties}
        if inherits_from:
            type_data['inherits_from'] = inherits_from
        data[type_name] = type_data
        base_types[type_name] = inherits_from
    return data, base_types

def remove_inherited(data, base_types):
    def get_all_inherited_methods_and_properties(type_name):
        if type_name not in data or 'inherits_from' not in data[type_name]:
            return {}, {}

        base_type = data[type_name]['inherits_from']
        if base_type not in data:
            return {}, {}

        base_methods, base_properties = get_all_inherited_methods_and_properties(base_type)

        base_methods.update(data[base_type]['methods'])
        base_properties.update(data[base_type]['properties'])

        return base_methods, base_properties

    for type_name, type_data in data.items():
        if 'inherits_from' in type_data:
            all_inherited_methods, all_inherited_properties = get_all_inherited_methods_and_properties(type_name)

            methods_to_remove = [method for method in type_data['methods'] if method in all_inherited_methods]
            properties_to_remove = [prop for prop in type_data['properties'] if prop in all_inherited_properties]

            for method in methods_to_remove:
                del type_data['methods'][method]
            for prop in properties_to_remove:
                del type_data['properties'][prop]

    return data

def compare_versions(old_data, new_data):
    changes = []
    old_types = old_data.keys()
    new_types = new_data.keys()

    for type_name in new_types:
        print(f'Checking type {type_name}')

        typeChanges = []
        inherits_from = new_data[type_name].get('inherits_from')
        min_changes = 2 if inherits_from else 1

        typeChanges.append(f'## {type_name}')
        if inherits_from:
            typeChanges.append(f'Inherits from: [{inherits_from}](#{inherits_from})')
        
        if type_name not in old_data:
            typeChanges.append(f'Added new type: `{type_name}`')
            continue

        old_methods = old_data[type_name]['methods']
        new_methods = new_data[type_name]['methods']
        old_properties = old_data[type_name]['properties']
        new_properties = new_data[type_name]['properties']

        # Compare methods
        for method_name, parameters in new_methods.items():
            if method_name not in old_methods:
                typeChanges.append(f'- New method added: `{method_name}`')
            elif old_methods[method_name] != parameters:
                typeChanges.append(f'- Method `{method_name}` changed parameters: ')
                for old_param, new_param in zip(old_methods[method_name], parameters):
                    if old_param != new_param:
                        typeChanges.append(f'  - Parameter `{old_param[0]}` changed type from `{old_param[1]}` to `{new_param[1]}`')

                for old_param in old_methods[method_name][len(parameters):]:
                    typeChanges.append(f'  - Parameter `{old_param[0]}` removed')

                for new_param in parameters[len(old_methods[method_name]):]:
                    typeChanges.append(f'  - New parameter added: `{new_param[0]}` of type `{new_param[1]}`')

        for method_name in old_methods:
            if method_name not in new_methods:
                typeChanges.append(f'- Method `{method_name}` removed from `{type_name}`')

        # Compare properties
        for property_name, property_type in new_properties.items():
            if property_name not in old_properties:
                typeChanges.append(f'- New property added in `{type_name}`: `{property_name}` of type `{property_type}`')
            elif old_properties[property_name] != property_type:
                typeChanges.append(f'- Property `{property_name}` in `{type_name}` changed type from `{old_properties[property_name]}` to `{property_type}`')

        for property_name in old_properties:
            if property_name not in new_properties:
                typeChanges.append(f'- Property `{property_name}` removed from `{type_name}`')

        if len(typeChanges) > min_changes:
            print(typeChanges)
            changes.extend(typeChanges)

    for type_name in old_types:
        if type_name not in new_data:
            changes.append(f'## {type_name}')
            changes.append(f'- Type removed')

    return changes

if __name__ == '__main__':
    old_file = sys.argv[1]
    new_file = sys.argv[2]
    changes_file = sys.argv[3]

    old_data, old_base_types = parse_xml(old_file)
    new_data, new_base_types = parse_xml(new_file)

    old_data = remove_inherited(old_data, old_base_types)
    new_data = remove_inherited(new_data, new_base_types)

    changes = compare_versions(old_data, new_data)

    with open(changes_file, 'w') as f:
        f.write('# Changes\n')
        for change in changes:
            f.write(f'{change}\n')
