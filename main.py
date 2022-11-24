from functions.libs import *

locations = getallfiles('data/location/')
place = choice(locations)

# account.create('Lyof')
# account.poke_add('Lyof', generate_place(place))
generate_place(place)

test = Pokemon()
print(test.data, test.savepath)
test.load('users/pokemons/lyof.0.json')
print(test.data, test.savepath)
test.save('data/temp.json')