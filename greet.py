

def greet(names):
    if names is None:
        names = 'my friend'

    if type(names) == list and len(names) == 2:
        return 'Hello, ' + ' and '.join(names) + '.'

    if type(names) == list and len(names) > 2:
        comma_separated = ', '.join(names[:-1])
        return 'Hello, {}, and {}.'.format(comma_separated, names[-1])

    if names.upper() == names:
        return 'HELLO {}!'.format(names)

    return 'Hello, {}.'.format(names)
