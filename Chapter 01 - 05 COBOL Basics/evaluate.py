vowels = ['a', 'e', 'i', 'o', 'u']
digits = ['0','1','2','3','4','5','6','7','8','9']


ch = input("Enter a character: ")

while ch.isalnum():
    if ch.lower() in vowels:
        print(ch, "is a Vowel")
    elif ch not in digits:
        print(ch, "is a Consonant")
    else:
        print(ch, "is a Digit")
    ch = input("Enter a character: ")
