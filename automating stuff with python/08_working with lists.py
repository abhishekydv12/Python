magicians = ['abhishek','shivam','rahul']
for magician in magicians:
    # print(magician.title() ,", that was a great trick ")
    # or you can write it this way 
    print(f"{magician.title()} that was a great trick")
    print(f"I can't wait to see your next trick, {magician.title()}")
print("Thank you everyone that was a great magic show")
# use the break statement if you want to stop the for loop in this case it will return only abhishek after using the break statement 
# working of a loop  
# first loop look into the list magicians and print the first element of the list which is assigned to the variable magician
# loop will do this multiple times line by line until printing of the last element 

cubes = []
for cube in range(1,11):
    cubes.append(cube**3) 
print(cubes)

# using list comprehensions
multiples = [multiple**3 for multiple in range(1,11)]
print(multiples)   


string = 'abhishek got placed into apple'
s = string.split()  #split each part of the string and store into a list 
print(s)  

# list of cubes from 1 to 10 including it using list comprehensions 
cubes = [cube**3 for cube in range(1,11)]  
print(cubes)

x = ['abhishek','sonal','shivam']
print(x[0:3:2])        # 2 means we have to skip 2 spaces which is one element into the given list so in return we will get 'abhishek','shivam' .
print(x[0:2])

# copying a list 
my_food = ["whey","eggs","broccoli","oats"]
my_friend = my_food[:]
my_food.append("vegetables")
my_friend.append("pizza")
for food in my_food:
    print(food.title(), end = ', ')  # we use end = to append the string at the end of the output and use ', ' for the gap between the items of the list 

print(f"my friend's food items are {my_friend}")

# try it yourself 
my_food = ["whey","eggs","broccoli","oats"]
my_friends = my_food[:]
print(f"the first three items in the list are {my_food[0:4]}")
print(f"the two items from the middle are {my_food[1:4]}")
print(f"the last three items in the list are {my_food[0:4]}")

# try it yourself 
pizzas = ["Peproni","cheese","chicken dominator"]
friend_pizza = pizzas[:]
pizzas.append("Paneer")
friend_pizza.append("capsicum")
print("my favourite pizzas are :")
for pizza in pizzas:
    print(pizza.title())
print("my friends favourite pizzas are :")
for pizza in friend_pizza:
    print(pizza.title())

# more loops
# foods.py name of python program
foods = ["vegetables","chapati","eggs"]
fast_food = ["burger","pizza","fries"]
for food in foods:
    print(food)
for food in fast_food:
    print(food)


