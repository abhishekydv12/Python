n = int(input("Enter any integer value here"))
int_value = map(int,input().split())
t = tuple(int_value)         #converting it into the tuple 
print(type(t))      #     this will be the class map 
print(hash(t))
