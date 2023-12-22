name = input("Please Enter your name :")
print(f"\nHello, {name}")

# adding condition into it 
age = input("Enter your age :")
age = int(age)      # for taking user input as an integer 
if age >= 23:
    print("you are good to ride")
else:
    print("you are not old enough to ride")

# #rental car 
rental_car = input("Enter car model you like : ")
print(f"let me see if i can find a {rental_car}")


# restaurant seatings
user = int(input("how many people are there in your group :"))

if user  >= 8:
    print("you guys have to wait for the table")

else:
    print("Table is ready")


# the modulo operator 
# a = 5 
# b =  17
# print(a%b)  # output will be 4  and for 3%6 output will be 3 and so on these cases 


# while loop in action

correct_number = 1
while correct_number < 3:
    print(correct_number)
    correct_number += 1



# try it yourself 
# multiples of ten 
INPUT = int(input("Enter any integer value :"))
if INPUT % 5 == 0 :
    print("Multiple of 10")
else:
    print("Not a Multiple of 10")

