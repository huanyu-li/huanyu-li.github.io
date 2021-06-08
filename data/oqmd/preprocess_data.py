import json
from collections import defaultdict

def read_json_file(file='oqmd-128K.json'):
    with open(file) as f:
        data = json.load(f)
        return data

def write_json(file_name, data):
	with open(file_name, 'w') as fp:
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
    entry_id = record['entry_id']
    calculation_id = record['calculation_id']
    composition_generic = record['composition_generic']
    name = record['name']
    spacegroup = record['spacegroup']
    band_gap = record['band_gap']
    delta_e = record['delta_e']
    calculations_dict['data'].append({'entry_id': entry_id, 'calculation_id': calculation_id})
    structures_dict['data'].append({'entry_id': entry_id, 'calculation_id': calculation_id})
    compositions_dict['data'].append({'entry_id': entry_id, 'calculation_id': calculation_id, 'name':name})
    spacegroups_dict['data'].append({'entry_id': entry_id, 'calculation_id': calculation_id, 'spacegroup': spacegroup})
    band_gaps_dict['data'].append({'entry_id': entry_id, 'calculation_id': calculation_id, 'band_gap': band_gap})
    formation_energies_dict['data'].append({'entry_id': entry_id, 'calculation_id': calculation_id, 'delta_e': delta_e})
    # write files
write_json('oqmd-calculation-128K.json', calculations_dict)
write_json('oqmd-structure-128K.json', structures_dict)
write_json('oqmd-composition-128K.json', compositions_dict)
write_json('oqmd-spacegroup-128K.json', spacegroups_dict)
write_json('oqmd-bandgap-128K.json', band_gaps_dict)
write_json('oqmd-formationenergy-128K.json', formation_energies_dict)
    