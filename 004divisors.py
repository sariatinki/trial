userinput = int(input("Enter a number:"))
divisors = []
for digit in range(1, userinput):
    if userinput % digit == 0:
        divisors.append(digit)
print(divisors)
