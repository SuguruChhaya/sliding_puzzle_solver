
#*I am trying to make a function to change the variables.
#*This works great!!
#!I have to initialize upbool to be self.upbool though
class Whatever():

    def __init__(self):
        self.a = True
        self.b = False

    def change(self, a=True, b=True):
        self.a = a
        self.b = b


    def next(self):
        self.change(a=False)
        print(self.a)
        print(self.b)

c = Whatever()
c.next()

