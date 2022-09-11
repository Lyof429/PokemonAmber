from functions.libs import *

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
    return load(open(path))

def setdata(path, value):
    strvalue = dumps(value, indent = 4)
    open(path, 'w').write(strvalue)

def upfirst(text):
    return text[0].upper() + text[1:len(text)]

def show(path, console=True):
    plt.imshow(img.imread(path))
    plt.show()

def getallfiles(path, ending='.json', sub=''):
    result = []
    for i in os.listdir(path):
        if len(i.split('.')) < 2:
            result += getallfiles(path+i, sub=i+'/')
        elif ending in i:
            result.append(sub+i.replace(ending, ''))
    return result