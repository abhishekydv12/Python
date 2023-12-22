cars = ["audi","range rover","bmw","rolls royce","lamborghini"]
for car in cars :
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# case sensitive
car = "Audi"
if car.lower() == "audi":        #shows case sensitive 
    print("True")
else:
    print("False")            

# conditional test 
a = "ab"
print('is a == "ab" ? i predict True')
print(a == 'ab')

car = 'range rover'
print('is car = "range rover" ? i think it is True')
print(car == "range rover")

print("is car == 'bmw' i predict it false")
print(car == "bmw")

book = "everything"
print('i predict book == "everything" is True')
print(book == "everything")

# 5-2 conditional test 
a = "abhishek"
b = "Abhishek"
if a == b:
    print("True")
else:
    print("False")
if b.lower() == a :   #using lower method 
    print("True")
else:
    print("False")

# numerical test 
a = 34
b = 56
if a >= 35 and b == 56:  # using and here 
    print("True")
else:
    print("False")

a = 20
b = 21
if a >= 19 or b != 21: # using or keyword
    print("True")
else:
    print("False")


# testing wheather a element in a list or not 
list = ["abhishek","sonal","geet k meena"]
if "abhishek" in list:
    print("True")
else:
    print("False")

# test wheather an item in not in a list [list of strings]
books = ["subtitle art of not giving a f*ck","steve jobs","demon slayer"]
if "demon slayer" not in books:
    print("True")
else:
    print("False")

# if without else
age = 19
if age >= 19:
    print("you are old enough to vote !")
    print("Have you registered to vote yet?")

# note if the condition is not matched this program will produce no output 

# using if-elif-else conditions
# amusement park problem
if age <= 4:
    print("Your admission cost is $0")
elif age <=18:
    print("Your admission fee is $25")
else:
    print("Your admission cost is $40")

# or we can write it this way
age = 4
if age <= 4:
    price = 0
elif age <= 18:
    price = 25
else:
    price = 40
print(f"your admission cost is ${price}")

# using multiple elif conditions into the code 
age = 65
if age <= 4:
    price = 0
elif age <= 18:
    price = 20
elif age >= 64:
    price = 15
else:
    price = 40
print(f"your admission fees is ${price}")

# try it yourself
alien_color = "green"
if alien_color == "green":
    print("you just earned 5 points")
# condition 2 
if alien_color == "red":
    print("your one enemy is out of game")

# 5-4 tryityourself
if alien_color == "green":
    print("you just earned 5 points")
else:
    print("you just earned 10 points")

alien_color = "red"
if alien_color == "blue":
    print("your one enemy is out of the game")
else:
    print("you are loosing at your end")

if alien_color == "red":
    print("you are about to win this game")
else:
    print("your enemy is winning this round")


# 5-5 tryit yourself  (using if - elif condition only)
alien = "green"
if alien == "green":
    print("you just earned 5 points")
elif alien == "yellow":
    print("you just earned 10 points")
elif alien == "red":
    print("you just earned 15 points")

# 5-6  
# mistake to avoid - use or instead of and 
age = int(input("Enter any age:"))
if age < 2:
    person = "baby"
elif  age == 2 or age < 4: 
    person = "toddler"
elif age == 4 or age < 13:
    person = "kid"
elif age == 13 or age < 20 :
    person = "teenager"
elif age <= 65:
    person = "adult"
else:
    person = "old"
print(f"he is {person}")

# 5-7  tryityourself 
favourite_fruits = ["mango","apple","banana","grapes"]
for fruit in favourite_fruits:
    print(fruit)
