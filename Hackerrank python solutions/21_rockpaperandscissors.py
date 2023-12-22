# rock, paper and scissors with computer 
print("rock...")
print("paper...")
print("scissor...")

from random import randint 
player = input("player, make your move : ").lower() 
random_number = randint(0,2) 
if random_number == 0: 
    computer = "rock"
elif random_number == 1: 
    computer = "paper"
else: 
    computer = "scissors"

print(f"computer plays {computer}")

if player == computer: 
    print("it's a tie")
elif player == "rock" : 
    if computer == "scissors" : 
        print("player wins") 
    elif computer == "paper": 
        print("computer wins") 
elif player == "paper" : 
    if computer == "rock" : 
        print("player wins") 
    elif computer == "scissors": 
        print("computer wins") 
elif player == "scissors" : 
    if computer == "paper" : 
        print("player wins") 
    elif computer == "rock": 
        print("computer wins") 
else : 
    print("something went wrong")


