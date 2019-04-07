num1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
userinput = int(input("Enter a number:"))
newlist = []
userlist = []
for no in num1:
    if no <= 5:
        newlist.append(no)
    if no <= userinput:
        userlist.append(no)
print(newlist)
print(userlist)

print([element for element in num1 if element <= 5])
