import random 

random_number = random.randint(1,10) 
guess = None

while guess != random_number: 
    guess = int(input("pick a number from 1 to 10: "))
    if random_number < guess: 
        print("too low")  
    elif random_number > guess: 
        print("too high")
    else: 
        print("you won !!")

print(random_number)