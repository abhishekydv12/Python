a = int(input("Enter any integer"))
b = int(input("Enter any integer"))

list1 = [a,b]      #contains a,b input into list 
for i in list1:
    print(i*"*")
exit()         #to exit from the loop

# we can use items instead of i

arr = [45,56]
for i in arr:
    print("*"*i)
exit()