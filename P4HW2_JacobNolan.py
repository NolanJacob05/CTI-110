# Nolan Jacob
# 10/23/24
# P4HW2
# Find Payrate of Employees

total_employees = 0
total_gross = 0 
total_OT = 0
total_reg = 0

# Get information from user
name = input("Enter employee's name or 'Exit' to terminate: ").capitalize()
while name.lower() != "exit":
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
    print()
    print("---" *15)
    print(f"{'Employee Name:' :<20} {name:<20}")
    print()
    print(f"{'Hours Worked':<12} {'Pay Rate':<12} {'Overtime':<12} {'Overtime Pay':<12} {'RegHour Pay':<12} {'Gross Pay':<12}")
    print("-----" *15)
    print(f"{hours:<12} ${payrate:<11} {overtime:<12} ${overtime_pay:<11.2f} ${reg_pay:<11.2f} ${gross_pay:<11.2f}")
    print()

    #Calculate total pay amounts
    total_employees += 1 
    total_OT = total_OT + overtime_pay
    total_reg = total_reg + reg_pay
    total_gross = total_gross + gross_pay

    #Ask user for new input
    name = input("Enter employee's name or 'Exit' to terminate: ").capitalize()

# Print totals to user
print()
print(f"Total number of employees entered: {total_employees}")
print(f"Total ammount paid for overtime: ${total_OT:.2f}")
print(f"Total ammount paid for regular hours: ${total_reg:.2f}")
print(f"Total ammount paid in gross: ${total_gross:.2f}")
