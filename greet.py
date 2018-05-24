

def format_names(names):
    if len(names) == 2:
        return ' and '.join(names)
    elif len(names) > 2:
        comma_separated = ', '.join(names[:-1])
        return '{}, and {}'.format(comma_separated, names[-1])
    elif len(names) == 1:
        return '{}'.format(names[0])
    return ''


def format_greeting(prefix, names, postfix):
    if len(names) > 0:
        return prefix + format_names(names) + postfix
    return ''


def greet(names):
    if names is None:
        names = ['my friend']

    if type(names) != list:
        names = [names]

    splitted_names = []
    for name in names:
        splitted_names.extend([name_part.strip() for name_part in name.split(',')])

    names = splitted_names
    normal_list = [name for name in names if not name.isupper()]
    shout_list = [name for name in names if name.isupper()]

    normal_greeting = format_greeting('Hello, ', normal_list, '.')
    shout_greeting = format_greeting('HELLO ', shout_list, '!')

    if len(normal_greeting) > 0 and len(shout_greeting):
        shout_greeting = ' AND ' + shout_greeting

    return normal_greeting + shout_greeting
