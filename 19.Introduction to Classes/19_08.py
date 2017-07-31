#  19_08

class Animal(object):
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print self.name
        print self.age
