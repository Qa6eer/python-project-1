a = float(input("Enter the first side (a): "))
b = float(input("Enter the second side (b): "))
c = float(input("Enter the third side (c): "))

if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print("The triangle is equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is isosceles.")
    elif a != b and b != c and a != c:
        print("The triangle is scalene.")
else:
    print("The triangle is not valid.")
