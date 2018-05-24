

def greet(name):
    if name is None:
        name = 'my friend'

    if type(name) == list:
        return 'Hello, ' + ' and '.join(name) + '.'

    if name.upper() == name:
        return 'HELLO {}!'.format(name)

    return 'Hello, {}.'.format(name)
