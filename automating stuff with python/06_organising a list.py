# organising a list 
cars = ['BMW','Mercedes','RollsRoyce','Audi']
# sort function  = used for organising a list into alphabetical order permanently 
cars.sort()
print(cars)
# in normal cases but not necessary = list is only sorted when the all the items of the list are either in uppercase or lowercase 
# cars = ['Bmw','audi','mercedes','rollsroyce']
# cars.sort()  #   this will not sort the list as Bmw first letter is in uppercase 
# print(cars)

# reversing the alphabetical order of the list 
bikes = ['ducati','bmw','ktm','royalenfield']
bikes.sort() #sorting the list in alphabetical order (increasing order)
bikes.sort(reverse = True)  # reversing the alphabetical order of the list 
print(bikes)

# sorting a list temporarily with sorted() method 
flowers = ['sunflower','jasmine','rose','lily']
print(sorted(flowers))# sorting list temporarily
print(flowers)

print("\nHere is the sorted list of flowers :") # \n is new line character used to indicate the end of a line text  
print(sorted(flowers))

print("Here is the original list again :")
print(flowers)

# list in reverse order
sports = ['cricket','badminton','football','wrestling']
sports.reverse() # reverse changes the order permanently but you can get it back by applying reverse in the nxt line or the program
sports.reverse() # returns orginal order of the list 
print(sports)

#finding the length of the list 
sports = ['cricket','badminton','football','wrestling']
# note = we use len function for finding the no of elements into the list 
# note = python counts the no of elements into the list starting with zero so to keep no erros when determining the length of the list 
print(len(sports))

# tryityourself problem
places = ['dubai','las vegas','maldives','hawai','paris']
print(places)
print(sorted(places))
print(f"Here is the original list {places}")
# places.sort(reverse = True)  #  sort and reverse the list permanently 
print(sorted(places))
places.reverse()  #  using reverse function twice to keep the list in the original state
places.reverse()
print(places)
places.reverse()
places.sort()
print(places)
places.sort(reverse = True)
print(places)
print(len(places))   # returns the length of the list 
# print(places[5])    returns index out of range because python show first item as 0 and then 1 and so on 
