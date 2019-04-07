phrase = input("Enter a phrase:")
new_phrase = phrase.split()
new_phrase.reverse()
reversed = ' '.join(new_phrase)
if phrase == reversed:
    print("It is a Palindrome")
else:
    print("Not a Palindrome")

