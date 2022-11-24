from functions.utils import *


class Pokemon:
    def __init__(self, data=None, path=None):
        if data is None:
            data = getdata()
        if path is None:
            path = 'data/temp.json'
        self.data = data
        self.savepath = path

    def load(self, path):
        self.data = getdata(path)
        self.savepath = path
        return self

    def save(self, path=None):
        if path is not None:
            self.savepath = path
        setdata(self.savepath, self.data)

    def hp(self):
        return self.data['fight']['stats']['pv']

    def get_stat(self, stat):
        return self.data['fight']['stats'][stat]