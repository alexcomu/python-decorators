from termcolor import colored
print colored("\n*** Lesson 8", "yellow")
print colored("## Class decorators!\n", "green")

class mydecorator(object):
    def __init__(self, before_text, after_text):
        self.before_text = before_text
        self.after_text = after_text

    def __call__(self, f):
        def newfunc():
            print self.before_text
            f()
            print self.after_text
        return newfunc

mydecorator1 = mydecorator('Hello', 'Goodbye')

@mydecorator1
@mydecorator('Before', 'After')
def myfunc():
    print 'INSIDE'

myfunc()

