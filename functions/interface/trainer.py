from functions.libs import *

defaultdata = {'info': {'name': '', 'poke_index': 0},
               'bag': {'pokeball': 5, 'pokedollar': 1000}}

def exists(trainer):
    return os.path.exists(f'users/{trainer.lower()}.json')

def create(trainer):
    if not exists(trainer):
        trainer_data = defaultdata
        trainer_data['info']['name'] = trainer.lower()
        setdata(f'users/{trainer.lower()}.json', trainer_data)

def delete(trainer):
    reset(trainer, True)
    os.remove(f'users/{trainer.lower()}.json')

def reset(trainer, delete=False):
    if delete:
        index = get(trainer)['info']['poke_index']
        for i in range(index):
            os.remove(f'users/pokemons/{trainer.lower()}.{i}.json')
    os.remove(f'users/{trainer.lower()}.json')
    create(trainer)

def get(trainer):
    return getdata(f'users/{trainer.lower()}.json')

def add(trainer, item, amount=1):
    trainer = get(trainer)
    trainer['bag'][item] = max(trainer['bag'][item]+amount if item in trainer['bag'].keys() else amount, 0)
    setdata(f'users/{trainer["info"]["name"].lower()}.json', trainer)

def has(trainer, item, amount=1):
    trainer = get(trainer)
    if item in trainer['bag'].keys() and trainer['bag'][item] >= amount:
        return True
    else:
        print(f"Vous n'avez pas assez de {upfirst(item)}s!")
        return False

def buy(trainer, item, amount=1):
    item_data = getdata(f'data/item/{item}.json')
    price = item_data['price']
    if has(trainer, 'pokedollar', price*amount):
        add(trainer, item.split('/')[-1], amount)
        add(trainer, 'pokedollar', -price*amount)