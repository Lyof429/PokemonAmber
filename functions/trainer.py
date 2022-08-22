from functions.libs import *

def reset(trainer):
    trainer = getdata(f'users/{trainer}/info.json')
    trainer['poke_index'] = 0
    setdata(f'users/{trainer["name"]}/info.json', trainer)
    setdata(f'users/{trainer["name"]}/bag.json', {})

def add(trainer, item, amount = 1):
    bag = getdata(f'users/{trainer}/bag.json')
    bag[item] = max(bag[item]+amount if item in bag.keys() else amount, 0)
    setdata(f'users/{trainer}/bag.json', bag)

def has(trainer, item, amount = 1):
    bag = getdata(f'users/{trainer}/bag.json')
    return item in bag.keys() and bag[item] >= amount