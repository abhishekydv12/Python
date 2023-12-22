# a simple dictionary
game = {"alien_o" : "green", "alien_x" : 45}
print(game["alien_o"])    #returns the value of alien_o stored into dictionary
print(game["alien_x"])  #same case here 
# if the alien is shooted in the game then
new_coins = game["alien_x"]   #value is 45 stored into dictionary 
print(f"congratulation you just earned {new_coins} coins")


# dictionary is associated with key value 
# each key is associated with a value in dictionary 
dict = {
    'abishek':'sonal',
    'rahul':'manali',
    'amit': 'anita',
    'sunita':'amarjeet'
}   

# for name,partner in dict.items():
#     print(name,partner)

# # to return only value output as follows :
# for value in dict.values():
#     print(f"this is the value stored into key {value}")

# for names,partners in dict.items():
#     for name in names:  # we use this statement for dict in dict statements 
#         print(name)


# for list in dictionary we use 
dict2 = {
    'abhishek': [12,23,45],
    'sonal':[12,23,46],
    'rahul':[35,67,78]
}

print(dict2)
for names,favourite_numbers in dict2.items():
    print(f"{names}'s favourite numbers are :")
    for favourite_number in favourite_numbers:
        print(f"\t {favourite_number}")


# for only one number from the list in dictionary
for names,numbers in dict2.items():
    print(f"{names}'s favourite number is  {numbers[0]}")
