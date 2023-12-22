s = input()
if len(s) >= 2 and s[:2] == "Is":      #remember we cannot use >= between string and integer
    print(s)
else:
    print("Is" + s)