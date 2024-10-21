char = input("Enter an alphabet: ").lower()

if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print(char, "is a vowel")

elif char.isalpha():
    print(char, "is a consonant")
    
else:
    print("Invalid input. Please enter an alphabet.")
