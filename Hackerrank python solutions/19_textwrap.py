import textwrap


string = input()
max_width = int(input())

for i in range(len(string)):

    s = textwrap.fill(string,max_width)
    print(s) 
    break; 

