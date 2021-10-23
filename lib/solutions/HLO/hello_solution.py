

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    try:
        return f'Hello, {str(friend_name)}!'
    except TypeError:
        return f'Hello, {friend_name}!'
