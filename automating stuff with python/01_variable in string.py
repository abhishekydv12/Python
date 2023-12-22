# a = "Abhishek"
# print(a.title())        # returns Abhishek
# print(a.upper())         # returns ABHISHEK
# print(a.lower())        #returns abhishek

first_name = "abhishek"
last_name = "yadav"
full_name = f"{first_name} {last_name}"   # introduced into python 3.6 ,before this  we use proper format method at place of f
print("Hello",full_name)   #returns Hello*variable's value
print(f"Hello, {full_name}")   #  returns Hello, abhishek yadav
txt = "{} {}".format(first_name,last_name)
message = f"Hello, {full_name.title()}"
# message = "{} {}".format(first_name,last_name)
print(message)
print(txt)
# text = "{} {}".format(first_name,last_name)   correct way of using the method 
# print(text)
# print("abhishek\nbody builder\nmr olympia")         use \n character to add a new line into string 

# \n denotes end of the line and \t denotes tab 
a = " abhishek\n\tcricket "
print(a.lstrip())      # removes whitespace from leftside 
print(a.rstrip())       # removes whitespace from right side
print(a.strip())       #removes the whitespace from both the sides 
print(a)

favourite_number = 12
leastfavourite_number = 78
fandl = favourite_number,leastfavourite_number
print(fandl)      # tuple = value of tuple cannot be changed 
message = "your favourite number is :"
print(message , fandl)
