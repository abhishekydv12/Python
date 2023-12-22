# How to add items to a list 
sweets = ['kajukatli','rasgulla','barfi']
sweets.append('gulabjamun')   #this will add one more item to the list at the end of it 
print(sweets)
sweets.insert(2,'khowa')    # even if we use double commas here python will automatically store this item into the list with single commas 
sweets.insert(3,'rasmalai')
# sweets.insert(2,3,'khowa','rasmalai')   # returns error because insert will take 2 arguments 
print(sweets)
# note = append take only one argument if we try to put more than one it will show error saying list.append() takes exactly one argument 
# sweets.append(1,'jalebi')   returns error 

# modifying list 
sweets[2] = 'jalebi'   # removes the previous items at 2 and add new item 'jalevi' at that place in the list 
print(sweets)


# removing items from the list 
# del,pop,remove used to remove items from a list 


motorcycle = ['Ducati','ktm','Hayabusa']
# motorcycle.pop() # removes  the last element of the list 
# motorcycle.pop(0) # removes 0th element from the list
print(motorcycle)

del motorcycle[2]  # removes 2the element from the list 
print(motorcycle)
# note = use del to remove item from the list we don't want to use further 
popped_variable = motorcycle.pop()
# note = use pop to remove item from the list at one time and want to use it further in the program 
# we can store that removed item into a variable named popped_variable for further use we can use it 
print(f" \n my favourite bike is {popped_variable.title()}")
print(motorcycle)


motorcycle.insert(2,'royal infield')      # we can use space in btw while writing string 
motorcycle.insert(3,'BMW model')
print(motorcycle)
