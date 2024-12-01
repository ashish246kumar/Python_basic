import time
# This generator function counts down from a given number `n` to 0, yielding each number one by one.
def countDown(n):
    while n>=0:
        yield n
        n=n-1
        time.sleep(1)

for count in countDown(5):
    print(count) 


#*********************************** Prime Number Generator*****************************
print("***********PRIME GENERATOR****************")
# Helper function to check if a number is prime.

def isPrime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True
# Generator function to produce an infinite sequence of prime numbers.

def prime_generator():
    num=2
    while True:
        if isPrime(num):
            yield num
        num+=1    
# Generates and prints the first 5 prime numbers.

prime_gen=prime_generator()
for i in range(5):
    print(next(prime_gen))

#************************Even Number  Generator****************************
print("***********EVEN NUMBER GENERATOR****************")
# Generator function to produce an infinite sequence of even numbers.
def even_generator():
    num=2
    while True:
        yield num
        num+=2
# Generates and prints the first 10 even numbers.
even_gen=even_generator()
for i in range(10):
    print(next(even_gen))


# *****************************Fibonacci Sequence Generator************************
print("***********FIBONACCI SEQUENCE GENERATOR****************")
# Generator function to produce the Fibonacci sequence indefinitely.
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
# Generates and prints the first 10 numbers in the Fibonacci sequence.
fib_gen=fibonacci()
for i in range(10):
    print(next(fib_gen))