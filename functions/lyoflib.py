from functions.libs import *

def chance(d):
    l = []
    for k in d.keys():
        for i in range(d[k]):
            l.append(k)
    return choice(l)

def randomize(mini, maxi):
    return random()*(maxi-mini) + mini

def getdata(path):
    return load(open(path))

def setdata(path, value):
    strvalue = dumps(value, indent = 4)
    open(path, 'w').write(strvalue)

def upfirst(text):
    return text[0].upper() + text[1:len(text)]