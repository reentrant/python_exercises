class Greeter:

    def __init__(self, boss):
        self.boss_name = boss
        self.greeting = None
        self.visitors = []

    def enters(self, visitor):
        if visitor == self.boss_name:
            self.greeting = "Hello, {}".format(visitor)
        else:
            self.visitors.append(visitor)

    def greet(self):
        greeting = None
        if self.greeting:
            greeting = self.greeting
            self.greeting = None
        else:
            if self.visitors:
                greeting = "Welcome, {}".format(self.visitors[-1])
        return greeting


g = Greeter('Chuck')
g.enters('Chuck')
print(g.greet())
print(g.greet())
g.enters('a')
g.enters('b')
print(g.greet())
