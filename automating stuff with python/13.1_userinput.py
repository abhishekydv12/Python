
a = "\n Enter any sentence and i will it after you"
a += "\n Enter 'quit' to enter from the loop :"

text = ""
while text != 'quit':
    # taking string as an input outside the while loop
    text = input(a)

    if text != 'quit':
        print(text)



# using a flag 
# flag = variable assigned for the program is active or not 

active = True
# active is variable and set to True so that program starts in active state 
while active :
    text = input(a)

    if text == 'quit':
        active = False    # making the state of program as false 
    else:
        print(text)

# using the break statement in Program 
x = "\n Enter the city you want to visit"
x += "\n Enter quit to quit the game"
while True:
    text = input(x)

    if text == 'quit':
        break  
    else:
        print(f"i would love to go to city {text.title()}")

# using continue inside a loop 

current_number = 0 
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0 :
        continue 


    print(current_number)
# note - according to the condition here when number is divisible by 2 and remainder is 0 then python ignores the loop 
# and then start from the beginning 





# avoiding the infinite loops
# this is the infinite loop which cannot stop 
# x = 1
# while x < 5:
#     print(x)

    # x += 1   value of x is increasing and loop will exit when value is greater than 5 or provided condition meets 


# try it yourself pizza toppings 

prompt = "\n Enter the topping you want to add"
prompt += "\n Enter 'quit' to end the process :"

topping = ""
while topping != 'quit':
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print(f"we'll add {topping} topping to your pizza")

#movie tickets try it yourself 

# note = error expected = < cannot supported btw int and str ( make sure age = int(input()))  as we are taking integer as an input from the user in program 
a = "\n Enter your age :"
age = int()
active = True  # state of program as active 
while age == int():
    age = int(input(a))

    if age < 3:
        ticket = "free"
    elif age >= 3 and age < 12:
        ticket = "$10"
    elif age >= 12:
        active = False       # making the state of program not active 
        ticket = "$15"
    else: 
        break

    print(ticket)

# writing the never ending program 
a = "\n Enter your age :"

age = 12
while age == 12:
    print(age)