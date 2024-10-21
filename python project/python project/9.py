char = input("Enter a character: ")

if char.isalpha():
    print(char, "is an alphabet.")

elif char.isdigit():
    print(char, "is a digit.")
    
elif not char.isalnum(): 
    print(char, "is a special character.")

else:
    print("Invalid input. Please enter a single character.")
