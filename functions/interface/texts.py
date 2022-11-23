from functions.libs import *


def dialog(file, trainer=None):
    file = open(f'assets/dialogs/{file}.txt').read()

    if trainer is not None:
        trainer_name = account.get(trainer)['info']['name']
        file = file.replace('@trainername', upfirst(trainer_name))

    for line in file.split('\n'):
        input(line)