# defining the function hello 
from asyncio import start_server
import re
from tkinter import Variable
from unicodedata import name
from unittest import FunctionTestCase

from pkg_resources import EGG_DIST


def hello(): 
    print('abhishek')
    print('abhishek is in usa')
    print('abhishek is working for house_of_innovation')
    print('Hello there')

hello()   #calling the hello function
hello()

# def statement with parameters 


# here name is the parameter -->(variables that have arguments assigned are called parameters) 
def hello(name): 
    print('hello, ' + name)

hello('abhishek')  #passing the argument to hello
hello('sonal')
# print(name)   --> gives nameerror 


# another example 
def sayhello(name): 
    print('hello, ' + name)

sayhello('abhishek')


# return values and return statements 

# definition - the value that a function call evaluates to its called the return value of function 

import random

def getAnswer(answernumber): 
    if answernumber == 1: 
        return 'it is certain'
    elif answernumber == 2: 
        return 'It is decidedly so'
    elif answernumber == 3: 
        return 'Yes'
    elif answernumber == 4: 
        return 'replay hazy try again'
    elif answernumber == 5: 
        return 'ask again later'
    elif answernumber == 6: 
        return 'Concentrate and ask again'
    elif answernumber == 7: 
        return 'myreply is no'
    elif answernumber == 8: 
        return 'outlook is not so good'
    elif answernumber == 9: 
        return 'very doubtful'


# random.randint is for selection random digit in (a: int, b: int)
r = random.randint(1,10)
fortune = getAnswer(r)
print(fortune)


# we can write this in one line as follows: -
# print(getAnswer(random.randint(1,9)))







# the call stack 

# forming a stack with the base always a 



def a(): 
    print('a() starts')
    b()
    d()
    print('a() returns')

def b(): 
    print('b() starts')
    c()
    print('b() returns')

def c() : 
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()  # calling the function a




# Local and global scope 


# Local scope => parameters and variables that are assigned in a called Function 
# are called to exist in that function's local scope
# variable that exist in local scope is called local variable 


# Global scope => variables that are assigned outside all functions are said to be global scope
# variable that exist in global scope is called global Variable



# local variables cannot be used in global space  
# def spam(): 
#     eggs = 1232312

# spam() 
# print(eggs)




def spam() : 
    eggs = 99
    bacon()
    print(eggs) 
    # output = 99
    # reason => when the bacon() returns the local scope for that function is destroyed 
    # including its eggs value 

def bacon() : 
    ham = 101 
    eggs = 10

spam() 





# Global variables can be read from a local space  
def Engineer(): 
    print(person)

person = 'Abhishek is a deep learning expert'
Engineer() #calling the function







# Local and global variables with same name  
def spam() : 
    eggs = 'spam local'
    print(eggs)


def bacon() : 
    eggs = 'bacon local'
    print(eggs)
    spam() 
    print(eggs)


eggs = 'global'
bacon() 
print(eggs)



# Global statement  
def spam(): 
    global eggs       #  declaring eggs as global
    eggs = 'spam'

eggs = 'global'
spam() 
print(eggs)  # output will be spam cos we already declared eggs as global in def spam






# another example 
def spam() : 
    global eggs      # this is global
    eggs = 'spam'

def bacon() : 
    eggs = 'bacon'     # this is local

def ham() : 
    print(eggs)        # this is global

eggs = 42    # this is global
spam() 
print(eggs)         






# this will throws an error cos of execution of eggs before eggs assigned to anything
def spam() : 
    # print(eggs)
    eggs = 'spam local'

eggs = 'global'
spam()  

# exception handling  
# for detecting the programs handling them and then continue to run (for saving the program from crash)


spam() 
