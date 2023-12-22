a = input("Enter your name :")
l = list(a)
position = int(input("Enter position of ch"))
character = input("ch :")
l[position] = character
# x = l.split(" ")   list has no attribute split \
# now we will join the string 


# important - this will return the string after joining the elements of the list 
a = "".join(l)
print(a) 


# returns error : int object is not iterable 
# for x in len(l1):
#     print(x)
