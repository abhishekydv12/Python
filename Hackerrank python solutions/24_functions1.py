
# function saying hi
# def say_hi () : 
#     print("hi")
# say_hi() 



# def square_of_7() : 
#     print("i am before the return value")
#     return 7**2 
# result = square_of_7() 
# print(result) 




# coin flip function using random 
from random import random 
def coin_flip() : 
    #generate a random number from 0-1 
    r = random() 
    if r > 0.5 : 
        return "HEADS"
    else: 
        return "TAILS"
print(coin_flip()) 


def sum_of_odd(numbers) : 
    total =  0
    for num in numbers : 
        if num % 2 != 0 : 
            total = total + num 
    return total

print(sum_of_odd([1,3,4,5,7]))





#default parameters 
def add(a,b): 
    return a + b

def math(a,b, fun=add) : 
    return fun(a,b) # calling the add function in case of default 

def substract(a,b) : 
    return a - b

math(2,2) # 4 sum 
math(2,2, substract) # 0 

