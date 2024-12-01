# Fibonacci function with parameter passing  and return value

def find_fibonacci(n:int)->int:
    if n<=0:
        return -1
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        a=0
        b=1
        for i in range(2,n):
            a,b=b,a+b
           
        return b

num:int=23 
ans=find_fibonacci(23) 
if ans<0:
    print("Input number is not a positive integer")
else:
    print(f"Fibonacci of {num}:{ans}")




#function with default argument
def find_power(base:int,exponent=2)->int:
    return base**exponent
print(find_power(2))
print(find_power(2,8))

