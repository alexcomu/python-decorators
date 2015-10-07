from termcolor import colored
print colored("*************************************************","red")
print colored("Welcome to my Super fast Tutorial for PYTHON Decorators!","red")

print colored("\n*** Lesson 1", "yellow")
print colored("## Functions are Objects!", "green")

def add(x,y):
    print "_ ADD", x+y

def sub(x,y):
    print "_ SUB", x-y

def apply(func, x, y):
    print colored("- APPLY-FUNCTION", "blue")
    return  func(x,y)

apply(add,10,5)
apply(sub,10,5)


print colored("\n*** Lesson 2", "yellow")
print colored("## Closures!", "green")

def outer(x):
    def inner():
        print x
    return inner

print1 = outer(1)
print2 = outer(2)
print1()
print2()
