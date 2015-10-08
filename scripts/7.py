from termcolor import colored
print colored("\n*** Lesson 7", "yellow")
print colored("## Function decorators!\n", "green")

def mydecorator(f):
    def newfunc():
        print 'Before Func'
        f()
        print 'After Func'
    return newfunc

def mydecorator2(f):
    def newfunc():
        print "Before other Func"
        f()
        print "After other Func"
    return newfunc

@mydecorator
@mydecorator2
def myfunc():
    print 'Hello'

myfunc()


