'''
functions: a block of code that only runs when it's called. 
 - they can be passed in data
 - they can return results
'''
from datetime import datetime

'''
this function will print out
'hello world!'
'''
def hello_world():
    print("hello world!")

'''
this function will return the current time
'''
def get_time():
    return datetime.now()

# Call hello_word()
hello_world()

# get the current time and print it out
time = get_time()
print("current time: {}".format(time))