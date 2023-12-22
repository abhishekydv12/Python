# 5-7 try it yourself
favourite_fruits = ["mango","banana","apple","grapes"]
for fruit in favourite_fruits :
    print(fruit)
if "mango" in favourite_fruits:
    print("you really like mango")
if "banana" in favourite_fruits:
    print("you really like banana")
if "apple" in favourite_fruits:
    print("you really like apple")
if "grapes" in favourite_fruits:
    print("you really like grapes")

# pizza topping
requested_toppings = ["mushroom","onion","cheese","green pepper"]
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")
print("\nyour pizza is ready with additonal toppings")   #  \n is new line character which indicates end of line 
# if the pizza  restaurant is run out of green pepper :
for requested_topping in requested_toppings:
    if requested_topping == "green pepper":
        print("sorry we are out of green pepper right now")
    else:
        print(f"Adding {requested_topping}")
# using multiple lists:
available_toppings = ["cheese","frenchfries","tomato","capsicum"]
requested_toppings = ["mushroom","onion","cheese","green pepper"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"sorry we don't have {requested_topping}")

# 5-8 Hello admin 
usernames = ["abhishek","navneet","sb","yogi","admin"]
for username in usernames:
    if username == "admin":
        print("Hello admin,would you like to see a special report")
    else:
        print(f"{username} thankyou for logging in again")
# 5-9 no users 
no_user = []
if no_user:
    for user in no_user:
        print(f"Hello {user} thanks for logging in again")
else:
    print("we need to find some users")  
# Hence the list is empty it will return message of else statement
# removing the users from the list 
users = ["shivam","abhishek","rahul","navneet","sb"]
users.pop()        #removes the last item from the list 
users.remove("shivam")  # removes item by item from the list 
users.clear()   # clears the entire list 
print(len(users))
print(users)

# 5-10 
current_users = ["SONAL","SHIVAM","NAVNEET","YOGI","ABHISHEK"]
new_users = ["sb","sonal","deepali","shivam","rajat rana"]
for new_user in new_users:   #  looping through the new_users 
    if new_user in current_users:
        print(f"{new_user} please enter new username")
    else:
        print(f"{new_user} this username is available")

#making comparison case insensitive
# for this we need to make a copy of current_users containing the lowercase versions of all existing users 
# making copy_users new list a copy of current_users but all strings are in lowercase 
copy_users = ["sonal","shivam","navneet","yogi","abhishek"]
for user in copy_users:
    if user.lower() in current_users:
        print(f"{user} this username is not available")
    else:
        print(f"{user} this username is available")   #making program case insensitive 
        
# ordinal numbers --> numbers defining their position in a series or a list like 1st ,2nd ,3rd and so on
ordinal = list(range(1,10))
for number in ordinal:  # looping through the list 
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
# note = styling a list is very important code will look clean and simple and easy for anyone to read 
# for eg : if age < 4:  is better than age<4  

