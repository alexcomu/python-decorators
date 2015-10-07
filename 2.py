from termcolor import colored
print colored("\n*** Lesson 2", "yellow")
print colored("## Closures!\n", "green")

def outer(x):
    def inner():
        print x
    return inner

print1 = outer(1)
print2 = outer(2)
print1()
print2()
