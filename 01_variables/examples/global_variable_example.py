'''
This program will demonstrate global and local variables.
'''

# global variable
car_color = "red"

# demonstrate local scope
def print_local_car_color():
    # local variable
    car_color = 'blue'
    print('1: car color is {}'.format(car_color))

# demonstrate global scope
def print_global_car_color():
    print('2: car color is {}'.format(car_color))

# modify gloval variable inside a function
def modify_global_variable():
    global car_color
    car_color = 'orange'

print_local_car_color()
print_global_car_color()

print('3: car color is {}'.format(car_color))
modify_global_variable()
print('4: car color is {}'.format(car_color))

