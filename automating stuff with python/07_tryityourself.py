# 4-1 problem
from os import X_OK


pizzas = ['onion','cheese','chicken dominator']
for pizza in pizzas:     # we assign variable here pizza to each item into the list pizzas
    print(f"i like {pizza.title()} pizza")
    # print(pizza + " is very good in taste")  we can this also to add the statement 
print("i really like pizza a lot as i enjoyed it with my family and my friends")
print("i really love pizza")

# 4-2 problem
Animals = ['tiger','lion','cheetah']
for Animal in Animals :
    print(f"{Animal.title()} is good in hunting")
    # print(Animal)
print("these animals have a similarity which is they have great ability to hunt their prey")
print("these animals are rare to be seen while hunting")


# use of range function
for x in range(1,5):     #return only up to 4 when we use the range function doesnot return the last element of the range 
    print(x)
# using range to print a list of numbers 
numbers = list(range(23,779))
print(numbers)  # returns list from 23 to 778

# list comprehensions 
numbers = [value**3 for value in range(1,6)]    #  value is raised to the power of 3 one by one using the for loop (value is variable name which is assigned to each value inside the list which is then raised to the power of 3)
print(numbers)                     
# range function does not include the last element which is range(n) 
#  4-3 tryityourself
numbers = list(range(1,5))
for item in numbers :
    print(item)
# 4-4 problem
values = list(range(1,4))
for value in values:
    print(value)
# 4-5 tryit yourself
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
# 4-6 tryityourself
cube = []
for value in range(1,11):
    cube.append(value**3)          # appending values one by one into the list cube 
print(cube)         


list1 = [1,2,3,4,5]
for item in list1:
    print(item)