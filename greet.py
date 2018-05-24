

def greet(names):
    if names is None:
        names = ['my friend']

    if type(names) != list:
        names = [names]

    normal_list = [name for name in names if not name.isupper()]
    shout_list = [name for name in names if name.isupper()]

    normal_greeting = ''
    shout_greeting = ''

    if len(normal_list) == 2:
        normal_greeting = 'Hello, ' + ' and '.join(normal_list) + '.'
    elif len(normal_list) > 2:
        comma_separated = ', '.join(normal_list[:-1])
        normal_greeting  = 'Hello, {}, and {}.'.format(comma_separated, normal_list[-1])
    elif len(normal_list) == 1:
        normal_greeting = 'Hello, {}.'.format(normal_list[0])

    if len(shout_list) > 0:
        shout_greeting = 'HELLO {}!'.format(' '.join(shout_list))

    if len(normal_greeting) > 0 and len(shout_greeting):
        shout_greeting = ' AND ' + shout_greeting

    return normal_greeting + shout_greeting
