num1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist = []
userinput = int(input("Enter a number:"))
for no in num1:
    if no <= userinput:
        newlist.append(no)
print(newlist)
