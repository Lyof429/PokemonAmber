from functions.libs import *

locations = getallfiles('data/location/')
place = choice(locations)


generate(place, show=True)