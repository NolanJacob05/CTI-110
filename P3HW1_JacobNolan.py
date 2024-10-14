# Nolan Jacob
# 10/14/24
# P3HW1
# Using If/Else statements

# create empty list
grades = []

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))
print()

# Add variables to list
grades.append(module1)
grades.append(module2)
grades.append(module3)
grades.append(module4)
grades.append(module5)
grades.append(module6)

# display results
print("-----------Results-------------")
print(f"{'Lowest grade:':<15} {min(grades):<10}")
print(f"{'Highest grade:':<15} {max(grades):<10}")
print(f"{'Sum of grades:':<15} {sum(grades):<10}")
average = sum(grades)/len(grades)
print(f"{'Average:':<15} {average:<10.2f}")
print("--"* 16)

# Find letter grade
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
elif average < 60:
    letter_grade = "F"

print(f"Your grade is: {letter_grade}")
