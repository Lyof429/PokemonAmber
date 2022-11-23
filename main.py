from functions.libs import *

locations = getallfiles('data/location/')
place = choice(locations)


x = generate_place(place)
print(x)
print(generate_poke(x['info']['name'], x['leveling']['level']))