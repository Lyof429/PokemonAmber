from functions.libs import *

defaultbag = {'pokeball': 5, 'pokedollar': 1000}

def exists(trainer):
    return os.path.exists(f'users/{trainer.lower()}.json')
def create(trainer):
    if not exists(trainer):
        setdata(f'users/{trainer.lower()}.json', {'info': {'name': trainer.lower(), 'poke_index': 0}, 'bag': defaultbag})
def delete(trainer):
    reset(trainer, True)
    os.remove(f'users/{trainer.lower()}.json')

def reset(trainer, delete=False):
    if delete:
        index = getdata(f'users/{trainer.lower()}.json')['info']['poke_index']
        for i in range(index):
            os.remove(f'users/pokemons/{trainer.lower()}.{i}.json')
    setdata(f'users/{trainer.lower()}.json', {'info': {'name': trainer.lower(), 'poke_index': 0}, 'bag': defaultbag})

def add(trainer, item, amount=1):
    trainer = getdata(f'users/{trainer.lower()}.json')
    trainer['bag'][item] = max(trainer['bag'][item]+amount if item in trainer['bag'].keys() else amount, 0)
    setdata(f'users/{trainer["info"]["name"].lower()}.json', trainer)

def has(trainer, item, amount=1):
    trainer = getdata(f'users/{trainer.lower()}.json')
    if item in trainer['bag'].keys() and trainer['bag'][item] >= amount:
        return True
    else:
        print(f"Vous n'avez pas assez de {upfirst(item)}s!")
        return False

def buy(trainer, item, amount=1):
    trainer_data = getdata(f'users/{trainer.lower()}.json')
    item_data = getdata(f'data/item/{item}.json')
    price = item_data['price']
    if has(trainer, 'pokedollar', price*amount):
        if item.split('/')[-1] in trainer_data['bag'].keys():
            trainer_data['bag'][item.split('/')[-1]] += amount
        else:
            trainer_data['bag'][item.split('/')[-1]] = amount
        trainer_data['bag']['pokedollar'] -= price*amount
        setdata(f'users/{trainer.lower()}.json', trainer_data)