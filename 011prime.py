digit = int(input("Enter a Number:"))
for num in range(2, digit):
    if digit%num == 0:
        result = "not prime"
        
    else:
        result = "prime"
print(result)

