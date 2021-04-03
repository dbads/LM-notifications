import sys
import traceback
from User import User
from Topic import Topic


def start():
  while True:
    command = input('Enter command $ ')
    print('command')
    [command_name, arg1, arg2] = command.split(' ')
    print(command_name, arg1, arg2)

    users = User()
    topics = Topic()

    try:
      # user actions
      if command_name == 'addUser':
        users.add_user({'role': arg2, 'username': arg1})
      elif command_name == 'removeUser':
        users.remove_user({'from_username': arg2, 'to_username': arg1})

      # topic actions
      elif command_name == 'addTopic':
        topics.add_topic({'username': arg1, 'topicname': arg2, 'users': users})
      elif command_name == 'removeTopic':
        topics.remove_topic({'username': arg1, 'topicname': arg2, 'users': users})

      elif command_name == 'resetUsers':
        users.reset()
      else:
        print('please input a valid command')
    except BaseException as ex:
      # Get current system exception
      ex_type, ex_value, ex_traceback = sys.exc_info()

      # Extract unformatter stack traces as tuples
      trace_back = traceback.extract_tb(ex_traceback)

      # Format stacktrace
      stack_trace = list()

      for trace in trace_back:
        stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" %
                           (trace[0], trace[1], trace[2], trace[3]))

        print("Exception type : %s " % ex_type.__name__)
        print("Exception message : %s" % ex_value)
        print("Stack trace : %s" % stack_trace)

    print('users in the system - ')
    print(users.users)
    print('topics in the system - ')
    print(topics.topics)


start()
