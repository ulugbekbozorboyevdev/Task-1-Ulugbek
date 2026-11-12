import string

code = input("Enter a code: ")

length = len(code)>=8
uppercase = any(char.isupper() for char in code)
digit= any(char.isdigit() for char in code) 
symbol = any(char in string.punctuation for char in code)

if length:
    print("Length: ✅")
else:
    print("Length: ❌(You should enter a code with more than 8 characters)")   

if uppercase:
    print("Uppercase: ✅")
else:
    print("Uppercase: ❌(You should enter at least one uppercase letter)")

if digit:
    print("Digit: ✅")
else:
    print("Digit: ❌(You should enter at least one digit)")

if symbol:
    print("Symbol: ✅")
else:
    print("Symbol: ❌(You should enter at least one symbol)")

score = sum([length, uppercase, digit, symbol])
print(f"Your code score is: {score}/4")
if score == 4:
    print("Your code is strong! ✅")
elif score == 3 or score == 2:
    print("Your code is medium! ⚠️")
else:
    print("Your code is weak! ❌")