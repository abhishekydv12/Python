# try it yourself problem
# 3-4 Guest list 
guest_list = ['sonal','rahul','shivam']
print(f"Hello {guest_list[0].title()} i would like to invite you for a dinner at my home ")
print(f"Hello {guest_list[1].title()} i would like to invite you for a dinner at my home ")
print(f"Hello {guest_list[-1].title()} i would like to invite you for a dinner at my home ")

# 3-5 changing Guest list 
print(f"Sorry guys but {guest_list[1].title()} will not be able to make it for the dinner ")
guest_list[1] = "geetkmeena"   # modifying the list by replacing the person who is not able to make it to dinner with new person 
print(f"Hello {guest_list[0].title()} you are invited for dinner at my home ")
print(f"Hello {guest_list[1].title()} you are invited for dinner at my home ")
print(f"Hello {guest_list[-1].title()} you are invited for dinner at my home ")

# 3-6 more guests
print(f"Hey guys {guest_list} i just found a bigger dining table for dinner i think we should invite more people for dinner ")
guest_list.insert(0,'ashish')
guest_list.insert(2,'rahul')
guest_list.append('trancekigalti')
print(guest_list)
message = "you are invited for dinner at my home at 8pm"
print(f"Hello {guest_list[0].title()} {message}")
print(f"Hello {guest_list[1].title()} {message}")
print(f"Hello {guest_list[2].title()} {message}")
print(f"Hello {guest_list[3].title()} {message}")
print(f"Hello {guest_list[4].title()} {message}")
print(f"Hello {guest_list[5].title()} {message}")
print(len(guest_list))

# 3-7 shrinking guest list 
txt = "Sorry guys  the plan is changed now i can only invite two people for dinner "
print(f"txt")
txt1 = "i am really sorry for this incovenience to you "
popped_person = guest_list.pop()
print(f"Hello {popped_person.title()} {txt1}")
popped_person = guest_list.pop()
print(f"Hello {popped_person.title()} {txt1}")
popped_person  = guest_list.pop()
print(f"Hello {popped_person.title()} {txt1}")
popped_person = guest_list.pop()
print(f"Hello {popped_person.title()} {txt1}")

print("Hello" + guest_list[0] + "you are still invited to the dinner at my home ")
print("Hello" + guest_list[1].title() + "you are still invited to the dinner at my home ")

print(len(guest_list))
del guest_list[0]
del guest_list[0]
print(guest_list)
print(len(guest_list)) # len is length of list hence it  is 0 means no element in guest_list
