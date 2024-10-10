grade_value = int(input("Enter your numbered grade: "))

if grade_value > 100:
    print("Invalid grade")
elif grade_value == 100:
    print("You scored a 100! A+")
elif grade_value >= 89:
    print("Your grade is an A")
elif grade_value >= 79:
    print("Your grade is a B")
elif grade_value >= 69:
    print("Your grade is a C")
elif grade_value >= 59:
    print("Your grade is a D")
elif grade_value >= 49:
    print("Your grade is an F")
elif grade_value >= 0:
    print("You failed")
elif grade_value <= 0:
    print("Invalid grade. Try Again")
else:
    print("Invalid grade")