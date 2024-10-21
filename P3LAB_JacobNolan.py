# Nolan Jacob
# 10/21/24
# P3LAB
# Calculating most efficient way to sort change

total = float(input("Enter the amount of money as a float: "))

# find the ammount of dollars
total = round(total * 100)
dollars = total // 100
dollars = int(dollars)
if dollars > 1:
    print(f"{dollars} Dollars")
elif dollars == 1:
    print(f"{dollars} Dollar")
else:
    pass

# Find ammount of quarters
coins = total % 100
quarters = coins // 25
quarters = int(quarters)
if quarters > 1:
    print(f"{quarters} Quarters")
elif quarters == 1:
    print(f"{quarters} Quarter")
else:
    pass

#Find ammount of dimes
coins = coins - quarters * 25
dimes = coins // 10
dimes = int(dimes)
if dimes > 1:
    print(f"{dimes} Dimes")
elif dimes == 1:
    print(f"{dimes} Dime")
else:
    pass

# Find ammount of nickels
coins = coins - dimes * 10
nickels = coins // 5
nickels = int(nickels)
if nickels > 1:
    print(f"{nickels} Nickels")
elif nickels == 1:
    print(f"{nickels} Nickel")
else:
    pass

# Find ammount of pennies
coins = coins - nickels * 5
pennies = coins // 1
pennies = int(pennies)
if pennies > 1:
    print(f"{pennies} Pennies")
elif pennies == 1:
    print(f"{pennies} Penny")
else:
    pass

# display no change if 0 dollars is entered
if dollars < 1 and quarters < 1 and dimes < 1 and nickels < 1 and pennies < 1:
    print("No Change")
else:
    pass
