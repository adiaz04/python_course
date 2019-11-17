
'''
Classes: An object constructor for creating objects.
'''


'''
Define a class with one attribute, named MySimpleClass
'''
# class MySimpleClass:
#     name = "MySimpleClass"

# my_class = MySimpleClass()
# print(my_class.name)


'''
Define a class with an init function which requires 
a parameter representing the name to be passed in.
'''
class MySimpleClass:
    def __init__(self, name):
        self.name = name

class1 = MySimpleClass("Class 1")
class2 = MySimpleClass("Class 2")

print(class1.name)
print(class2.name)
