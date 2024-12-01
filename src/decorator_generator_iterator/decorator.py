
import time
import math
#simple decorator example
# This decorator demonstrates how to execute additional logic before and after a function call.
def simple_decorator(func):
    def wrapper(*args,**kwargs):
        print("Before function call")
        result = func(*args,**kwargs)
        print("After function call")
        return result
    return wrapper

# Applying the simple_decorator to the greet function using the @ syntax
@simple_decorator
def greet(name):
    #  Function to print a greeting message.
    # Decorated to include additional behavior before and after execution.
    print(f"Hello, {name}")

greet("abc")

#*****************************************Generator Example*********************************
# This decorator calculates the time taken by the decorated function to execute.

def calculateTime(func):
    def innerFunc(*args,**kwargs):
        startTime=time.time()
        func(*args,**kwargs)
        endTime=time.time()
        print(f"Time taken by {func.__name__} is {endTime-startTime} seconds")
    return innerFunc   
 
# Applying the calculateTime decorator to the factorial function

@calculateTime
def factorial(num):
    
    # Function to calculate and print the factorial of a given number.
    # Decorated to measure the time taken to execute the function.
    print(f"factorial of {num} is:{math.factorial(num)}")
    time.sleep(5)
factorial(5)
