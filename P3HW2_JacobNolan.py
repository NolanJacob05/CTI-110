# Nolan Jacob
# 10/23/24
# P3HW2
# Find Payrate of Employees

# Get information from user
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
payrate = float(input("Enter employee's pay rate: "))

#calculate payrate
if hours <= 40:
    overtime = 0
    overtime_pay = 0
    reg_pay = (hours * payrate)
    gross_pay = reg_pay + overtime_pay

elif hours > 40:
    overtime =(hours - 40)
    overtime_pay = (overtime * 1.5) * payrate
    reg_pay = (hours - overtime) * payrate
    gross_pay = reg_pay + overtime_pay

#Display payrate to user

print("---" *15)
print(f"{'Employee Name:' :<20} {name:<20}")
print()
print(f"{'Hours Worked':<12} {'Pay Rate':<12} {'Overtime':<12} {'Overtime Pay':<12} {'RegHour Pay':<12} {'Gross Pay':<12}")
print("-----" *15)
print(f"{hours:<12} ${payrate:<11} {overtime:<12} ${overtime_pay:<11.2f} ${reg_pay:<11.2f} ${gross_pay:<11.2f}")
