import json
from collections import defaultdict

def read_json_file(file='mp-128K.json'):
    with open(file) as f:
        data = json.load(f)
        return data

def write_json(file_formula_pretty, data):
	with open(file_formula_pretty, 'w') as fp:
		json.dump(data, fp)


calculation_lst = []
calculations_dict = defaultdict(list)
structure_lst = []
structures_dict = defaultdict(list)
composition_lst = []
compositions_dict = defaultdict(list)
spacegroup_lst = []
spacegroups_dict = defaultdict(list)
band_gap_lst = []
band_gaps_dict = defaultdict(list)
formation_energy_lst = []
formation_energies_dict = defaultdict(list)

returned_data = read_json_file()

for record in returned_data['data']:
    material_id = record['material_id']
    #composition_generic = record['composition_generic']
    formula_pretty = record['formula_pretty']
    spacegroup = record['spacegroup']['symbol']
    band_gap = record['band_gap']
    energy = record['energy']
    calculations_dict['data'].append({'material_id': material_id})
    structures_dict['data'].append({'material_id': material_id})
    compositions_dict['data'].append({'material_id': material_id, 'formula_pretty':formula_pretty})
    spacegroups_dict['data'].append({'material_id': material_id, 'spacegroup': spacegroup})
    band_gaps_dict['data'].append({'material_id': material_id, 'band_gap': band_gap})
    formation_energies_dict['data'].append({'material_id': material_id, 'energy': energy})
    # write files
write_json('mp-calculation-128K.json', calculations_dict)
write_json('mp-structure-128K.json', structures_dict)
write_json('mp-composition-128K.json', compositions_dict)
write_json('mp-spacegroup-128K.json', spacegroups_dict)
write_json('mp-bandgap-128K.json', band_gaps_dict)
write_json('mp-formationenergy-128K.json', formation_energies_dict)
    