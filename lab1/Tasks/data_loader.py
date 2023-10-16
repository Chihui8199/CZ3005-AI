import json
import os

_data = {
    'G': None,
    'Dist': None,
    'Cost': None,
    'Coord': None
}

# Get the path to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate to the parent directory and then into the "Data" folder
data_dir = os.path.join(script_dir, '..', 'Data')

def load_data():
    global _data

    if _data['G'] is None:
        with open(os.path.join(data_dir, 'G.json'), 'r') as file:
            _data['G'] = json.load(file)

    if _data['Dist'] is None:
        with open(os.path.join(data_dir, 'Dist.json'), 'r') as file:
            _data['Dist'] = json.load(file)

    if _data['Cost'] is None:
        with open(os.path.join(data_dir, 'Cost.json'), 'r') as file:
            _data['Cost'] = json.load(file)

    if _data['Coord'] is None:
        with open(os.path.join(data_dir, 'Coord.json'), 'r') as file:
            _data['Coord'] = json.load(file)

    return _data['G'], _data['Dist'], _data['Cost'], _data['Coord']
