a = int(input("Enter the marks in Physics: "))
b = int(input("Enter the marks in Chemistry: "))
c = int(input("Enter the marks in Biology: "))
d = int(input("Enter the marks in Mathematics: "))
e = int(input("Enter the marks in Computer: "))

print("Maximum Marks = 500")

marks_obtained = a + b + c + d + e
print("Marks Obtained =" , marks_obtained)

total_marks = 500

if (marks_obtained / total_marks) * 100 >= 33:
    print("Student has passed!")
else:
    print("Student has not passed!")

percentage = (marks_obtained / total_marks) * 100
print("And the percentage is", percentage, "%")

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print("Grade obtained is:", grade)
