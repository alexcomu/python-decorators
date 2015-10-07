from termcolor import colored
print colored("\n*** Lesson 4", "yellow")
print colored("## Decorators in real Life!\n", "green")

class Coordinate(object):
     def __init__(self, x, y):
         self.x = x
         self.y = y
     def __repr__(self):
         return "Coord: " + str(self.__dict__)

def add(a, b):
     return Coordinate(a.x + b.x, a.y + b.y)
def sub(a, b):
     return Coordinate(a.x - b.x, a.y - b.y)

one = Coordinate(100,200)
two = Coordinate(500,300)

print colored("Simple Call","blue")
print add(one,two)

print colored("But.. what if I would like to insert some checks?For example what if result should be limited to positive coordinates)", "blue")
print colored("I can use some Wrapper function!", "blue")

def wrapper(func):
    # used to prevent no-positive values
    def checker(a, b):
        if a.x < 0 or a.y < 0:
             a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
             b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
             ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret
    return checker

one = Coordinate(100, 200)
two = Coordinate(300, 200)
three = Coordinate(-100, -100)

add = wrapper(add)
sub = wrapper(sub)
print sub(one, two)
print add(one, three)
