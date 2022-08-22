from functions.libs import *

genWild('route/route1.json')
add('Uju', 'pokeball')
getCatch(1, getdata('data/temp.json')['fight']['stats']['pv'], 'pokeball', 1, 'Uju')
addxp(10000, 'users/Uju/pokemons/0.json')