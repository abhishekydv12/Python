from random import random 
def coin_flip() : 
    #generate a random number from 0-1 
    r = random() 
    if r > 0.5: 
        return "HEADS"
    else: 
        return "TAILS"
print(coin_flip()) 