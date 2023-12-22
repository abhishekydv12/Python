# tuples = list we cannot change throughout the program or we say immutable list 
# we use parenthesis  () instead of square bracket []
Dimensions = (200,50)
print(Dimensions[0])
print(Dimensions[1])
#Dimensions[1] = 250  # cannot change the value of a tuple python throws an error when we try to print the above program
print(Dimensions)

# looping through a tuple
dimension = (100,400)
for value in dimension:
    print(value)

# writing over a tuple 
dimension = (200,500)
for dimension in dimension:
    print(dimension)

modified_dimension = (400,500)
for dimension in modified_dimension:
    print(dimension)

# note = tuples are simple data structures we use them when we want to store a set of variable that is not changed throughout the program

# 9-13try it yourself
five_basic_foods = ("daal","roti","rice","salad","sabji")
for food in five_basic_foods:
    print(food)
# five_basic_foods[1] = "fish"
print("change in menu as follows:")
five_basic_foods = ("fish","vegetable","pulav")
for food in five_basic_foods:
    print(food)


