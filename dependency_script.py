import json
import csv 

with open('dependencies.json') as json_data: 
    data = json.load(json_data) 

libraries_to_optypes = {} 

with open('optypes_to_libraries.csv', 'w', newline='') as csvfile:
    fieldnames = ['Operation Type', 'Libraries Used', 'Number of Libraries Used'] 
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for operation_type in data['op_types']: 
        libraries = data['op_types'][operation_type]['references']['libraries']
        writer.writerow({
                            'Operation Type': operation_type,
                            'Libraries Used': libraries,
                            'Number of Libraries Used': len(libraries)
                        })

        for lib in libaries: 
            if lib in libraries_to_optypes: 
                libraries_to_optypes[lib].append(operation_type) 
            else: 
                libraries_to_optypes[lib] = [operation_type] 

for library in data['libraries']:
    print(library) 
    if library not in libraries_to_optypes:
        libraries_to_optypes[library] = []

with open('libraries_to_optypes.csv', 'w', newline='') as csvfile: 
    fieldnames = ['Library', 'Operation Types', 'Number of OpTypes Citing Library']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 

    writer.writeheader()

    for lib in libraries_to_optypes:
        writer.writerow({
                            'Library': lib,
                            'Operation Types': libraries_to_optypes[lib], 
                            'Number of OpTypes Citing Library': len(libraries_to_optypes[lib])
                        })
    

