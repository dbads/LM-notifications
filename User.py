class User:
  users = {}

  def __str__(self):
    return self.users

  def __init__(self):
    pass

  def add_user(self, user):
    username = user['username']
    if not username in self.users:
      self.users[username] = {
          'role': user['role']
      }
      print('User added successfully')
    else:
      print('User already exists')

  def remove_user(self, to_user, from_user):
    from_username = from_user['username']
    to_username = to_user['username']

    # validate command issuer
    if not from_username in self.users:
      print('Error, only a valid admin user can remove other users')
    if from_user.role != 'admin':
      print('Permission Error, only admin users can remove other users')

    # an admin can nto delete him/herself
    if from_username == to_username:
      print('Can not delete yourself')

    # perform deletion
    if not to_username in self.users:
      print('Error, The user to be removed doesn\'t exit')
    else:
      del self.users[to_username]
      print('User deleted successfully')

  # for development purpose
  def subscribe_topic(self, data):
    username = data['username']
    topicname = data['topicname']

    if not username in self.users:
      print('User does not exist')
    else:
      if not 'topics' in self.users[username]:
          self.users[username]['topics'] = {topicname: {}}
      else:
        self.users[username]['topics'][topicname] = {}


  # for development purpose
  def reset(self):
    self.users = {}
