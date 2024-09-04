grades = input("Enter three grades: ").split()
grade1, grade2, grade3 = map(float, grades)

ave = (grade1 + grade2 + grade3) / 3
print(f"Average grade: {ave:.2f}")

if ave >= 98 and ave <= 100:
    print("With Highest Honor")
elif ave >= 95 and ave <= 97:
    print("With High Honor")
elif ave >= 90 and ave <= 94:
    print("With Honor")
elif ave >= 75 and ave <= 89:
    print("Passed")
elif ave >= 74 and ave <= 51:
    print("Failed")
elif ave > 100 and ave <= 50:
    print("Invalid grade")
else:
    print("Error")