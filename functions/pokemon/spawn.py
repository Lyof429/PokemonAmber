from functions.libs import *

def generate(place, path = 'data/temp.json', show = False):
    place_data = getdata(f'data/location/{place}.json')
    
    name = chance(place_data['pokemons'])
    if not os.path.exists(f'data/pokemon/{name.lower()}.json'): return {}
    poke_data = getdata(f'data/pokemon/{name.lower()}.json')
    
    bonus = ''
    if 'variants' in poke_data.keys():
        bonus += chance(poke_data['variants'])
    if random() < 0.02:
        bonus += ' Shiny'
    
    gender = ' '
    if 'gender' in poke_data.keys():
        gender = (' ♀ ', ' ♂ ')[random() < poke_data['gender']]
        
    lvl = randint(place_data['level_range']['min'], place_data['level_range']['max'])
    
    a = [i for i in poke_data['attacks'].keys() if poke_data['attacks'][i] <= lvl]
    attacks = ''
    for i in range(min(4, len(a))):
        j = randint(0, len(a)-1)
        attacks += f'{a[j]} - '
        del a[j]
    del a
    attacks = attacks[0:len(attacks)-3]
    
    ability = chance(poke_data['abilities'])

    result = {'info': {'name': name,
                       'nickname': '',
                       'other': bonus,
                       'gender': gender.replace(' ', '')
                       },
              'leveling': {'level': lvl,
                           'xp': 0,
                           'type': poke_data['level_type'] if 'level_type' in poke_data.keys() else 'simple'
                           },
              'fight': {'ability': ability,
                        'attacks': attacks.split(' - '),
                        'stats': {}
                        }
              }
    setdata(path, result)
    refreshstats(path)
    if show:
        print(f'                                                                                   [{place_data["name"]}]\n'
              f'{name}{bonus}{gender} -  Lv {lvl} ({result["leveling"]["xp"]}/{getxpneed(result)})\n{ability}  |  {attacks}')
    else:
        print(f'[{place_data["name"]}] Un {name}{bonus} sauvage (Lv {lvl}) apparait!')
    return getdata(path)

def addxp(amount, path = 'data/temp.json'):
    poke_data = getdata(path)
    need = getxpneed(poke_data)
    poke_data['leveling']['xp'] += amount

    attacks = reverse(getdata(f'data/pokemon/{poke_data["info"]["name"].lower()}.json')['attacks'])
    while poke_data['leveling']['xp'] >= need:
        if poke_data['leveling']['level'] >= 100:
            poke_data['leveling']['level'] = 100
            break

        poke_data['leveling']['xp'] -= need
        poke_data['leveling']['level'] += 1
        print(f'{poke_data["info"]["name"]} passe au niveau {poke_data["leveling"]["level"]}!')
        for stat in poke_data['fight']['stats'].keys():
            poke_data['fight']['stats'][stat] += 2

        if poke_data['leveling']['level'] in attacks.keys():
            newattack = attacks[poke_data['leveling']['level']]
            if len(poke_data['fight']['attacks']) < 4:
                poke_data['fight']['attacks'].append(newattack)
                print(f'{poke_data["info"]["name"]} apprend {newattack}!')
            else:
                oldattack = input(f'{poke_data["info"]["name"]} veut apprendre {newattack}. Mais {poke_data["info"]["name"]} connait déjà 4 capacités.\nVoulez vous remplacer une capacité par {newattack}?     {each(poke_data["fight"]["attacks"])}\n')
                if oldattack in poke_data['fight']['attacks']:
                    del(poke_data['fight']['attacks'][poke_data['fight']['attacks'].index(oldattack)])
                    poke_data['fight']['attacks'].append(newattack)
                    print(f'{poke_data["info"]["name"]} oublie {oldattack} et apprend {newattack}!')
                else:
                    print(f'{poke_data["info"]["name"]} n\'a pas appris {newattack}.')

        need = getxpneed(poke_data)
    setdata(path, poke_data)
    #refreshstats(path)

def getxpneed(poke_data):
    if poke_data['leveling']['type'] == 'fast':
        need = 0.8 * (poke_data['leveling']['level'] ** 3)
    elif poke_data['leveling']['type'] == 'slow':
        need = 1.2 * (poke_data['leveling']['level'] ** 3)
    else: # if poke_data['leveling']['type'] == 'simple':
        need = poke_data['leveling']['level'] ** 3
    return round(need)

def refreshstats(path = 'data/temp.json'):
    name = getdata(path)['info']['name']
    poke_data = getdata(f'data/pokemon/{name.lower()}.json')
    temp_data = getdata(path)
    for stat in poke_data['stats'].keys():
        temp_data['fight']['stats'][stat] = maxstat(stat, path)
    setdata(path, temp_data)

def maxstat(stat, path = 'data/temp.json'):
    name = getdata(path)['info']['name']
    poke_data = getdata(f'data/pokemon/{name.lower()}.json')
    temp_data = getdata(path)
    return 2*(temp_data['leveling']['level']-1) + poke_data['stats'][stat]

def catch(ball='pokeball', trainer = None, path = 'data/temp.json'):
    if trainer is not None:
        if account.has(trainer, ball):
            account.add(trainer, ball, -1)
        else:
            return False
    
    pokemon = getdata(path)['info']['name']
    pvnow, pvmax = getdata(path)['fight']['stats']['pv'], maxstat('pv', path)
    status = getdata(path)['fight']['status'] if 'status' in getdata(path)['fight'].keys() else 1
    a = (1-(2/3)*(pvnow/pvmax))*getdata(f'data/pokemon/{pokemon.lower()}.json')['catch_rate']*getdata(f'data/item/ball/{ball.lower()}.json')['catch_bonus']*status
    b, n = 65535*((a/255)**0.25), 0
    for i in range(4):
        if randint(0, 65535) <= b:
            n += 1
            sleep(0.5)
            if n == 4:
                print(f'{pokemon} capturé!')
                result = True
            else:
                print('...')
    if n < 4:
        print(f'Zut! Ca y était presque!')
        result = False
    
    if trainer != None and result:
        pokemon = getdata(path)
        pokemon['info']['ball'] = ball
        pokemon['info']['nickname'] = input(f'Entrez le nom de votre {pokemon["info"]["name"]}: ')
        trainer = getdata(f'users/{trainer.lower()}.json')
        setdata(f'users/pokemons/{trainer["info"]["name"]}.{trainer["info"]["poke_index"]}.json', pokemon)
        trainer["info"]['poke_index'] += 1
        setdata(f'users/{trainer["info"]["name"]}.json', trainer)
    print('\n')
    return result