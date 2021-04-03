
class Topic:
  topics = {}

  def __init__(self):
    pass

  def add_topic(self, data):
    username = data['username']
    topicname = data['topicname']
    users = data['users'].users

    # permission check
    if not username in users or users[username]['role'] != 'admin':
      print('Only admins can create topics')

    self.topics[topicname] = {}
    print('Added new Topic')

  def remove_topic(self, data):
    username = data['username']
    topicname = data['topicname']
    users = data['users'].users

    # permission check
    if not username in users or users[username]['role'] != 'admin':
      print('Only admins can remove topics')

    del self.topics[topicname]
    print('Removed Topic')
