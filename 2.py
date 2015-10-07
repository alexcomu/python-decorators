from termcolor import colored
print colored("*************************************************","red")
print colored("Welcome to my Super fast Tutorial for PYTHON Decorators!","red")

print colored("\n*** Lesson 3", "yellow")
print colored("## Decorators!", "green")

def outer(some_func):
    def inner():
        print "before some_func"
        ret = some_func() # 1
        return ret + 1
    return inner

def foo():
    return 1

decorated = outer(foo) # 2
print decorated()

print colored("We could say that the variable decorated is a decorated version of foo", "blue")
print colored("- foo plus something", "blue")
