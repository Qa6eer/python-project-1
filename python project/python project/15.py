a = float(input("Enter the first side (a): "))
b = float(input("Enter the second side (b): "))
c = float(input("Enter the third side (c): "))

if a + b > c and a + c > b and b + c > a:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
