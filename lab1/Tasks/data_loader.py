import json
from pathlib import Path

_data = {
    'G': None,
    'Dist': None,
    'Cost': None
}


def load_data():
    global _data

    if _data['G'] is None:
        with open(Path('data') / 'G.json', 'r') as file:
            _data['G'] = json.load(file)

    if _data['Dist'] is None:
        with open(Path('data') / 'Dist.json', 'r') as file:
            _data['Dist'] = json.load(file)

    if _data['Cost'] is None:
        with open(Path('data') / 'Cost.json', 'r') as file:
            _data['Cost'] = json.load(file)

    return _data['G'], _data['Dist'], _data['Cost']
