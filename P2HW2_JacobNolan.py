# Nolan Jacob
# 10/9/24
# P2HW2
# using lists in python

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
