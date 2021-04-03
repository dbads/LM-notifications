from User import User

def start():
  while True:
    command = input('Enter command $ ')
    print('command')
    [command_name, arg1, arg2] = command.split(' ')
    print(command_name, arg1, arg2)

    if command_name == 'addUser':
      users = User({})
      users.add_user({'role': arg2, 'username': arg1})
    else:
      print('please input a valid command')

    print('users in the system - ')
    print(users.users)


start()