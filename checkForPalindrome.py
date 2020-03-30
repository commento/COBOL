inpt = input("enter a word: ")
inpt = inpt.lower()
if inpt == inpt[::-1]: print(inpt, "is palindrome")
else: print(inpt, "is not palindrome")