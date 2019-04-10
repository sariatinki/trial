#Write a program that asks the user how many Fibonnaci numbers to generate and
#then generates them. Take this opportunity to think about how you can use
#functions. Make sure to ask the user to enter the number of numbers in the
#sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers
#where the next number in the sequence is the sum of the previous two numbers
#in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def get_number(num = "Enter a number:"):
    return int(input(num))

series = get_number("Fibonnaci numbers to generate:")
first_num = get_number("The first number of the series:")
second_num = get_number()
fibonnaci = 0
print(first_num)
print(second_num)

while fibonnaci <= series:
    fibo = first_num + second_num
    first_num = second_num
    second_num = fibo
    fibonnaci += 1
    print(fibo)
    
    


