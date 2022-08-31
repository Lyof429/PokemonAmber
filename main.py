from functions.libs import *

generate('fearful_forest_entrance')
account.delete('Lyof')
account.add('Papatte', 'pokedollar', 10000)
account.buy('Papatte', 'ball/hyperball', 10)
catch('hyperball', trainer='Papatte')