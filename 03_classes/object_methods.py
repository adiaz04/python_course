class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def bio(self):
        print("hello, my name is {} and I'm {} years old.".format (self.name, self.age))

p1 = Person("Jeff", 44)
p1.bio()

p2 = Person("Joe", 33)
p2.bio()