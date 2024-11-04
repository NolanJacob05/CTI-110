# Nolan Jacob
# 11/4/24
# P4HW1
# using loops to calculate grades

# get number of scores from user
num_scores = int(input("How many scores do you want to enter? "))

# create list for scores
scorelist=[]

# for loop for user to enter grades
for score in range(0,num_scores):
    grade = float(input(f"Enter score #{score+1} "))

    while grade < 0 or grade > 100:
        print()
        print(f"INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        grade = float(input(f"Enter score #{score+1} again: "))

    # Enter score into list
    scorelist.append(grade)

print()
print()
# Print Results to user
print("---------------Results---------------")
print(f"{'Lowest Score':<15}: {min(scorelist)}")
scorelist.remove(min(scorelist))
print(f"{'Modified List':<15}: {scorelist}")
average = (sum(scorelist) / len(scorelist))
print(f"{'Average Score':<15}: {average:.2f}")

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

print(f"{'Grade':<15}: {letter_grade}")
print("-------------------------------------")
