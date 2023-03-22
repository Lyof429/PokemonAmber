import requests
import os
from pprint import pprint
from functions.utils import *


def get(url):
    reply = requests.get(url)
    if reply.status_code == 200:
        return reply.json()


def pokemon(name):
    raw = get('https://pokeapi.co/api/v2/pokemon/' + name)
    if raw is None:
        return
    raw['sprites'] = None


    new = {}

    new['name'] = raw['name'].title()

    new['gender'] = 0.5
    new['catch_rate'] = 100

    new['abilities'] = {}
    for a in raw['abilities']:
        c = 10 if len(a.keys()) == 2 else 5
        c = 1 if a['is_hidden'] else c
        new['abilities'][a['ability']['name'].title()] = c

    new['attacks'] = {}
    for m in raw['moves']:
        if m['version_group_details'][-1]['move_learn_method']['name'] == 'level-up':
            new['attacks'][m['move']['name'].title().replace('-', ' ')] = m['version_group_details'][-1][
                'level_learned_at']

    new['types'] = []
    for t in raw['types']:
        new['types'].append(t['type']['name'].title())

    stats = {'hp': 'pv', 'attack': 'atk', 'defense': 'def', 'special-attack': 'atkspe', 'special-defense': 'defspe', 'speed': 'spe'}
    new['stats'] = {}
    for s in raw['stats']:
        new['stats'][stats[s['stat']['name']]] = s['base_stat']


    if not os.path.exists(f'data/pokemon/{name}.json'):
        setdata(f'data/pokemon/{name}.json', new)