class User:
  users = None
  def __init__(self, users):
    if not self.users: self.users = users

  def add_user(self, user):
    username = user['username']
    if not username in self.users:
      self.users[username] = {
        'role': user['role']
      }
      print('User added successfully')
    else:
      print('User already exists')


  def remove_user(self, from_user, to_user):
    from_username = from_user.username
    form_user = self.users[from_username]
    to_username = to_user.username

    # validate command issuer
    if not from_username in self.users:
      print('Error, only a valid admin user can remove other users')
    if from_user.role != 'admin':
      print('Permission Error, only admin users can remove other users')

    # perform deletion
    if not to_username in self.users:
      print('Error, The user to be removed doesn\'t exit')
    else:
      del self.users[to_username]
      print('User deleted successfully')


