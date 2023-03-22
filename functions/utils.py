from random import choice, random
import json
import os
import matplotlib.pyplot
import matplotlib.image

def chance(d):
    l = []
    for k in d.keys():
        for i in range(d[k]):
            l.append(k)
    return choice(l)

def randomize(mini, maxi):
    return random()*(maxi-mini) + mini

def reverse(dict):
    return {i: a for a, i in dict.items()}

def each(l, sep = ' - '):
    result = ''
    for i in l:
        result += f'{i}{sep}'
    return result[0:len(result)-len(sep)]

def getdata(path = 'data/temp.json'):
    return json.load(open(path))

def setdata(path, value):
    strvalue = json.dumps(value, indent=4)
    open(path, 'w').write(strvalue)


def show(path):
    matplotlib.pyplot.imshow(matplotlib.image.imread(path))
    matplotlib.pyplot.show()

def getallfiles(path, useend=False, ending='.json', sub=''):
    result = []
    for i in os.listdir(path):
        if len(i.split('.')) < 2:
            result += getallfiles(path+i, sub=sub+i+'/')
        elif i.endswith(ending):
            result.append(sub+i if useend else sub+i.replace(ending, ''))
    return result