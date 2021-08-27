"""
HTML Generator
Return the decorator and the decorated function from the correct places in the new html() decorator.
Use the html() decorator to wrap the return value of hello() in the
strings <b> and </b> (the HTML tags that mean "bold").
Use html() to wrap the return value of goodbye() in the strings <i> and </i> (the HTML tags that mean "italics").

Use html() to wrap hello_goodbye() in a DIV, which is done by adding the strings <div> and </div> tags around a string.
"""

from functools import wraps


def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        msg = func(*args, **kwargs)
        return '<b>{}</b>'.format(msg)

    return wrapper


def italics(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        msg = func(*args, **kwargs)
        return '<i>{}</i>'.format(msg)

    return wrapper


def html(open_tag, close_tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            msg = func(*args, **kwargs)
            return '{}{}{}'.format(open_tag, msg, close_tag)

        # Return the decorated function
        return wrapper

    # Return the decorator
    return decorator


# Make hello() return bolded text
@html('<html>', '</html')
def hello(name):
    return 'Hello {}!'.format(name)


print(hello('Alice'))


# Make goodbye() return italicized text
@html('i', '/i')
def goodbye(name):
    return 'Goodbye {}.'.format(name)


print(goodbye('Alice'))


# Wrap the result of hello_goodbye() in <div> and </div>
@html('<div>', '</div>')
def hello_goodbye(name):
    return '\n{}\n{}\n'.format(hello(name), goodbye(name))


print(hello_goodbye('Alice'))
