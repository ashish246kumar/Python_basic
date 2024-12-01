# Example of if, elif, else statements: Check if a word is a palindrome
def is_palindrome(word:str)->None:
    if len(word)==0:
        print(f"The word '{word}' is empty")
    elif word==word[::-1]:
        print(f"The word '{word}' is palindromic")
    else:
        print(f"The word '{word}' is not palindromic")    

is_palindrome("madam")
is_palindrome("hello")
is_palindrome("")

#Square of number from 1 to 5
for i in range(1,6):
    print(f"Square of {i}->{i**2}")

#sum of all the even no from 1 to num
sum:int=0
num:int=10
incr:int=1
while(incr<=num):
    if incr%2==0:
        sum=sum+incr
    incr+=1
print(f"sum of all the even number from 1 to {num}={sum}")
