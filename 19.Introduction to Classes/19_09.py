#  19_09

class Animal(object):
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print self.name
        print self.age

hippo = Animal("hippo", 2)
sloth = Animal("sloth", 1)
ocelot = Animal("ocelot", 7)

print hippo.health
print sloth.health
print ocelot.health
