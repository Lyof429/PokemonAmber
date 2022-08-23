from functions.libs import *

genWild('route/route1.json')
account.create('Lyof')
getCatch(1, getdata()['fight']['stats']['pv'], 'pokeball', 1, 'Lyof')
account.delete('Lyof')