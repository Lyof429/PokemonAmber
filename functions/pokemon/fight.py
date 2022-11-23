from functions.libs import *

def getdamageold(lv, att, df, puis, cm):
    return round((((lv*0.4+2)*att*puis)/(df*50)+2)*cm*randomize(0.85, 1))

def getdamage(self, other, attackname):
    attackname = getid(attackname)
    self = getdata(self)
    other = getdata(other)
    
    if os.path.exists(f'data/attack/{attackname}.json'):
        attack = getdata(f'data/attack/{attackname}.json')
    else:
        attack = {'power': 60, 'precision': 100, 'category': '', 'type': 'Normal'}
    
    category = attack['category']
    power = attack['power']
    level = self['leveling']['level']
    attack_stat = self['fight']['stats'][f'atk{category}']
    defense_stat = other['fight']['stats'][f'def{category}']
    
    result = ((level*0.4+2)*attack_stat*power)/(defense_stat*50)+2
    result *= randomize(0.85, 1)
    if random() < 0.1:
        result *= 2
    result = round(result)
    
    return max(1, result)

def registerattacks(poke):
    baseattackdata = {'power': 60,
                      'precision': 100,
                      'category': '',
                      'type': 'Normal'}
    
    poke = getdata(poke)
    attacks = poke['fight']['attacks']
    for a in attacks:
        if a == '': return
        a = getid(a)
        print(a, os.path.exists(f'data/attack/{a}.json'))
        #if not os.path.exists(f'data/attack/{a}.json'):
        setdata(f'data/attack/{a}.json', baseattackdata)
