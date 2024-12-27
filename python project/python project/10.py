char = input("Enter an alphabet: ")

if char.isalpha():
    if char.isupper():
        print(char, "is an uppercase alphabet.")
    else:
        print(char, "is a lowercase alphabet.")
else:
    print("Invalid input! Please enter an alphabet.")
