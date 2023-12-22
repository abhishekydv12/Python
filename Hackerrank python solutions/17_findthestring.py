# have to find no of time sub_string into the string 
string = input().lower()
sub_string = input().lower()
x = 0

# we use 1 here for increasing the range of the function to the required string 
for i in range(0,len(string) - len(sub_string) + 1):
    print(i)
    # operation on strings (advanced concept for the strings in Python)
    if string[i:i + len(sub_string)] == sub_string:
        x += 1

print(x)


