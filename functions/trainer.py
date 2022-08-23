from functions.libs import *

def create(trainer):
    if not os.path.exists(f'users/{trainer.lower()}.json'):
        setdata(f'users/{trainer.lower()}.json', {'info': {'name': trainer.lower(), 'poke_index': 0}, 'bag': {'pokeball': 5}})
def delete(trainer):
    reset(trainer, True)
    os.remove(f'users/{trainer.lower()}.json')

def reset(trainer, delete = False):
    if delete:
        index = getdata(f'users/{trainer.lower()}.json')['info']['poke_index']
        for i in range(index):
            os.remove(f'users/pokemons/{trainer.lower()}.{i}.json')
    setdata(f'users/{trainer.lower()}.json', {'info': {'name': trainer, 'poke_index': 0}, 'bag': {'pokeball': 5}})

def add(trainer, item, amount = 1):
    trainer = getdata(f'users/{trainer.lower()}.json')
    trainer['bag'][item] = max(trainer['bag'][item]+amount if item in trainer['bag'].keys() else amount, 0)
    setdata(f'users/{trainer["info"]["name"].lower()}.json', trainer)

def has(trainer, item, amount = 1):
    trainer = getdata(f'users/{trainer.lower()}.json')
    return item in trainer['bag'].keys() and trainer['bag'][item] >= amount