1.Make a generator to perform the same functionality of the iterator
def generator(input):

    num=1

    for x in input:

        num=num*x

        yield x
      
for x in generator(5):  

    print(x) 
	
2.Try overwriting some default dunder methods and manipulate their default behavior
class Employee:

    def __init__(self, name,designation):

        self.name = name

        self.designation = designation

    
    def __str__(self):

        return "Employee Details are name: {} , designation: {} from {}".format(self.name, self.designation)

emp = Employee("Meetal","SA" )

print(emp)



3.Write a decorator that times a function call using timeit

#start a timer before func call
#end the timer after func call
#print the time diff

from functools import wraps
import time

def Decorator_Demo(func):

    @wraps(func)

    def timeitwrap(*args, **kwargs):

        start_time = time.perf_counter()

        print(f"Start time {start_time}")

        func(*args, **kwargs)

        end_time = time.perf_counter()

        print(f"end time {end_time}")

        print(f"time spend is {end_time-start_time}")

    return timeitwrap

