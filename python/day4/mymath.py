def add(a,b):
    return a+b

def subtact(a,b):
    return a-b


def divide(a,b):
    return a/b

def multiply(*args):
    total = 1

    for num in args:
        total *= num

    return total