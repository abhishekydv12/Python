if __name__ == '__main__':
    N = int(input("Enter any integer value :"))
    # Lists in Python - Hacker Rank Solution START
    Output = []; # list for storing the input from the user 
    for i in range(0,N):     # i has assigned values from 0 to the N one by one 
        ip = input().split()
        if ip[0] == "print":
            print(Output)
        elif ip[0] == "insert":
            Output.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == "remove":
            Output.remove(int(ip[1]))
        elif ip[0] == "pop":
            Output.pop()
        elif ip[0] == "append":
            Output.append(int(ip[1]))
        elif ip[0] == "sort":
            Output.sort()
        else:
            Output.reverse()