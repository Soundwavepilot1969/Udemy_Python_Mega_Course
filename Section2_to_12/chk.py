def foo(*args):
    new_list = [items.upper() for items in args]
    new_list.sort()
    return new_list

print(foo('we','er','aa'))