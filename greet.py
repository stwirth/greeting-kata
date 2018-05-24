

def greet(name):
    if name is None:
        name = 'my friend'

    if name.upper() == name:
        return 'HELLO {}!'.format(name)

    return 'Hello, {}.'.format(name)
