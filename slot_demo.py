class NormalClass:
    classvar = "foo"
    def __init__(self):
        self.x = 1
        self.y = 2

n = NormalClass()
print(n.__dict__)

class SlottedClass:
    __slots__ = ('x', 'y')
    classvars = 'foo'

    def __init__(self):
        self.z = 1

s = SlottedClass()
print(s.__dict__)
print(s.__slots__)
