from collections.abc import Container
# duck typing

def print_stuff(stuff):
    if isinstance(stuff, Container):
        for item in stuff:
            print(item)
    else:
        print(stuff)
    

items = ('spam', 'eggs', 'steak')

print(isinstance(items, tuple))
print(isinstance(items, list))
print(isinstance(items, Container))
print_stuff('abc')
print_stuff(123)
