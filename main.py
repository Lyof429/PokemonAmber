from functions.libs import *

# ----- TERMINAL CODE -----
user = ''
command = ''
while command != '.stop':
    command = input('POKEMON AMBER - .help for command list\n>> ')
    if command[0:6] == '.catch':
        args = command.split(' ')
        if len(args) > 2:
            catch(args[1], user, args[2])
        else:
            catch(args[1], user)
    elif command == '.help':
        print('.catch [pokeball] (path) >> Catch current wild Pokemon\n'
              '<.help >> Get commands list\n'
              '.map >> Show Anyl map\n'
              '.move [location] >> Go to another location\n'
              '.stop >> Stop the program\n'
              '.user [name] >> Set user'
              '.wild (path) >> Generate a Pokemon from your current location')
    elif command == '.map':
        show('assets/sprites/map.png')
    elif command[0:5] == '.move':
        if account.exists(user):
            user_data = getdata(f'users/{user.lower()}.json')
            if not 'game' in user_data.keys():
                user_data['game'] = {}
            user_data['game']['location'] = command[6:len(command)]
            setdata(f'users/{user.lower()}.json', user_data)
    elif command[0:5] == '.user':
        user = command[6:len(command)]
        account.create(user)
    elif command[0:5] == '.wild':
        args = command.split(' ')
        if len(args) > 1:
            generate(getdata(f'users/{user.lower()}.json')['game']['location'], args[1])
        else:
            generate(getdata(f'users/{user.lower()}.json')['game']['location'])