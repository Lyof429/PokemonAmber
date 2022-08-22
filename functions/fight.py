from functions.libs import *

def genWild(place):
    place_data = getdata(f'data/location/{place}')
    
    
    name = chance(place_data['pokemons'])
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
        del(a[j])
    del(a)
    attacks = attacks[0:len(attacks)-3]
    
    ability = chance(poke_data['abilities'])
    
    print(f'{name}{bonus}{gender} -  Lv {lvl}\n{ability}  |  {attacks}\n')
    RESULT = {'info': {'name': name, 'nickname': '', 'other': bonus, 'gender': gender.replace(' ', ''), 'level': lvl}, 'fight': {'ability': ability, 'attacks': attacks.split(' - '), 'stats': {}}}
    setdata('data/temp.json', RESULT)
    lvlstat()
    return RESULT

def lvlstat(path = 'data/temp.json'):
    name = getdata(path)['info']['name']
    pokemon_data = getdata(f'data/pokemon/{name.lower()}.json')
    temp_data = getdata(path)
    for stat in pokemon_data['stats'].keys():
        temp_data['fight']['stats'][stat] = 2*(temp_data['info']['level']-1) + pokemon_data['stats'][stat]
    setdata(path, temp_data)

def getDamage(lv, att, déf, puis, cm):
    return round((((lv*0.4+2)*att*puis)/(déf*50)+2)*cm*randomize(0.85, 1))       #(random()*0.15+0.85)

def getCatch(pvnow, pvmax, ball, status, trainer = None):
    if trainer != None:
        if has(trainer, ball):
            add(trainer, ball, -1)
        else:
            print(f"Vous n'avez plus de {upfirst(ball)}s!")
            return False
    
    pokemon = getdata('data/temp.json')['info']['name']
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
        pokemon = getdata('data/temp.json')
        pokemon['info']['ball'] = ball
        pokemon['info']['nickname'] = input(f'Entrez le nom de votre {pokemon["info"]["name"]}: ')
        trainer = getdata(f'users/{trainer}/info.json')
        setdata(f'users/{trainer["name"]}/pokemons/{trainer["poke_index"]}.json', pokemon)
        trainer['poke_index'] += 1
        setdata(f'users/{trainer["name"]}/info.json', trainer)
    return result